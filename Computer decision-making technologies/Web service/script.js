let criteria = [];
let alternatives = [];
let evaluations = [];
let currentRankings = [];
let resultsChart = null;

function setupCriteria() {
    const count = parseInt(document.getElementById('criteria-count').value);
    const container = document.getElementById('criteria-setup');
    
    let html = '<div class="table-wrapper"><table class="data-grid"><tr><th>Критерий</th>';
    for (let i = 0; i < count; i++) {
        html += `<th>K<sub>${i+1}</sub></th>`;
    }
    html += '</tr><tr><td style="color: #8ecae6;">Тип оптимизации</td>';
    
    for (let i = 0; i < count; i++) {
        html += `<td>
            <select id="crit-type-${i}" class="input-field" style="width: 100px; margin: 0 auto;">
                <option value="max">max ↑</option>
                <option value="min">min ↓</option>
            </select>
        </td>`;
    }
    html += '</tr></table></div>';
    
    container.innerHTML = html;
    
    if (count >= 4) {
        document.getElementById('crit-type-0').value = 'max';
        document.getElementById('crit-type-1').value = 'min';
        document.getElementById('crit-type-2').value = 'max';
        document.getElementById('crit-type-3').value = 'min';
    }
    
    showNotification('Критерии инвестиционной оценки настроены');
}

function setupAlternatives() {
    const altCount = parseInt(document.getElementById('alt-count').value);
    const critCount = parseInt(document.getElementById('criteria-count').value);
    const container = document.getElementById('input-table-container');
    
    let html = '<div class="table-wrapper"><table class="data-grid"><tr><th>IT-проект</th>';
    
    for (let j = 0; j < critCount; j++) {
        const critType = document.getElementById(`crit-type-${j}`)?.value || 'max';
        html += `<th>K<sub>${j+1}</sub><br><small>(${critType})</small></th>`;
    }
    html += '</tr>';
    
    for (let i = 0; i < altCount; i++) {
        html += `<tr><td style="color: #90e0ef; font-weight: bold;">a<sub>${i+1}</sub></td>`;
        for (let j = 0; j < critCount; j++) {
            html += `<td>
                <input type="number" 
                       id="eval-${i}-${j}" 
                       class="input-field" 
                       value="${getDefaultValue(i, j)}" 
                       step="0.1" 
                       style="width: 80px; margin: 0 auto; text-align: center;">
            </td>`;
        }
        html += '</tr>';
    }
    html += '</table></div>';
    
    container.innerHTML = html;
    showNotification('Таблица оценок IT-проектов готова');
}

function getDefaultValue(i, j) {
    const defaultValues = [
        [35, 24, 9, 3],
        [25, 18, 8, 5],
        [30, 12, 7, 4],
        [40, 36, 6, 8]
    ];
    return defaultValues[i] && defaultValues[i][j] !== undefined ? defaultValues[i][j] : 1;
}

function calculateAll() {
    const critCount = parseInt(document.getElementById('criteria-count').value);
    criteria = [];
    for (let i = 0; i < critCount; i++) {
        criteria.push({
            name: `K${i+1}`,
            type: document.getElementById(`crit-type-${i}`).value
        });
    }
    
    const altCount = parseInt(document.getElementById('alt-count').value);
    alternatives = [];
    evaluations = [];
    
    for (let i = 0; i < altCount; i++) {
        alternatives.push(`a${i+1}`);
        evaluations[i] = [];
        for (let j = 0; j < critCount; j++) {
            const value = parseFloat(document.getElementById(`eval-${i}-${j}`).value);
            evaluations[i][j] = isNaN(value) ? 0 : value;
        }
    }
    
    try {
        const preferenceMatrices = calculatePreferenceMatrices();
        displayPreferenceMatrices(preferenceMatrices);
        
        const sumMatrix = calculateSumMatrix(preferenceMatrices);
        displaySumMatrix(sumMatrix);
        
        const { adjacencyMatrix, weightMatrix } = calculateAdjacencyAndWeightMatrices(sumMatrix);
        displayAdjacencyMatrices(adjacencyMatrix, weightMatrix);
        
        currentRankings = calculateRankings(weightMatrix);
        displayRankings(currentRankings);
        
        drawChart(currentRankings);
        
        document.getElementById('matrices-section').style.display = 'block';
        document.getElementById('sum-section').style.display = 'block';
        document.getElementById('adjacency-section').style.display = 'block';
        document.getElementById('results-section').style.display = 'block';
        
        setTimeout(() => showLPRDialog(), 500);
        showNotification('Инвестиционный анализ успешно завершен!');
        
    } catch (error) {
        showNotification('Ошибка: ' + error.message);
    }
}

function calculatePreferenceMatrices() {
    const matrices = [];
    const n = alternatives.length;
    const m = criteria.length;
    
    for (let k = 0; k < m; k++) {
        const matrix = [];
        const critType = criteria[k].type;
        
        for (let i = 0; i < n; i++) {
            matrix[i] = [];
            for (let j = 0; j < n; j++) {
                if (i === j) {
                    matrix[i][j] = 0.5;
                } else {
                    const xi = evaluations[i][k];
                    const xj = evaluations[j][k];
                    
                    if (xi === 0 && xj === 0) {
                        matrix[i][j] = 0.5;
                    } else if (critType === 'max') {
                        matrix[i][j] = xj / (xi + xj);
                    } else {
                        matrix[i][j] = xi / (xi + xj);
                    }
                }
            }
        }
        matrices.push(matrix);
    }
    
    return matrices;
}

function displayPreferenceMatrices(matrices) {
    let html = '';
    
    matrices.forEach((matrix, idx) => {
        html += `
            <div class="matrix-container">
                <div class="matrix-title">
                    <span class="section-icon">📋</span>
                    Матрица P<sup>${idx+1}</sup> (${criteria[idx].name} - ${criteria[idx].type})
                </div>
                <div class="table-wrapper">
                    <table class="data-grid">
                        <tr><th></th>
        `;
        
        alternatives.forEach(alt => {
            html += `<th>${alt}</th>`;
        });
        html += '</tr>';
        
        matrix.forEach((row, i) => {
            html += `<tr><th style="color: #90e0ef;">${alternatives[i]}</th>`;
            row.forEach(cell => {
                const color = cell > 0.5 ? '#2ecc71' : cell < 0.5 ? '#e74c3c' : '#95a5a6';
                html += `<td style="color: ${color}; font-weight: ${cell !== 0.5 ? 'bold' : 'normal'};">${cell.toFixed(3)}</td>`;
            });
            html += '</tr>';
        });
        
        html += '</table></div></div>';
    });
    
    document.getElementById('preference-matrices').innerHTML = html;
}

function calculateSumMatrix(preferenceMatrices) {
    const n = alternatives.length;
    const sumMatrix = [];
    
    for (let i = 0; i < n; i++) {
        sumMatrix[i] = [];
        for (let j = 0; j < n; j++) {
            sumMatrix[i][j] = 0;
            preferenceMatrices.forEach(matrix => {
                sumMatrix[i][j] += matrix[i][j];
            });
        }
    }
    
    return sumMatrix;
}

function displaySumMatrix(sumMatrix) {
    let html = `
        <div class="matrix-container">
            <div class="matrix-title">
                <span class="section-icon">🧮</span>
                Суммарная матрица P<sub>Σ</sub>
            </div>
            <div class="table-wrapper">
                <table class="data-grid">
                    <tr><th></th>
    `;
    
    alternatives.forEach(alt => {
        html += `<th>${alt}</th>`;
    });
    html += '</tr>';
    
    sumMatrix.forEach((row, i) => {
        html += `<tr><th style="color: #90e0ef;">${alternatives[i]}</th>`;
        row.forEach(cell => {
            html += `<td>${cell.toFixed(3)}</td>`;
        });
        html += '</tr>';
    });
    html += '</table></div></div>';
    
    document.getElementById('sum-matrix').innerHTML = html;
}

function calculateAdjacencyAndWeightMatrices(sumMatrix) {
    const n = alternatives.length;
    const adjacencyMatrix = [];
    const weightMatrix = [];
    
    for (let i = 0; i < n; i++) {
        adjacencyMatrix[i] = [];
        weightMatrix[i] = [];
        for (let j = 0; j < n; j++) {
            const diff = sumMatrix[i][j] - sumMatrix[j][i];
            
            if (diff > 0) {
                adjacencyMatrix[i][j] = 1;
                weightMatrix[i][j] = diff;
            } else {
                adjacencyMatrix[i][j] = 0;
                weightMatrix[i][j] = 0;
            }
        }
    }
    
    return { adjacencyMatrix, weightMatrix };
}

function displayAdjacencyMatrices(adjacencyMatrix, weightMatrix) {
    let html = `
        <div style="margin-bottom: 30px;">
            <div class="matrix-title">
                <span class="section-icon">🔗</span>
                Матрица смежности R<sub>Σ</sub> (1 - есть связь, 0 - нет связи)
            </div>
            <div class="table-wrapper">
                <table class="data-grid">
                    <tr><th></th>
    `;
    
    alternatives.forEach(alt => {
        html += `<th>${alt}</th>`;
    });
    html += '</tr>';
    
    adjacencyMatrix.forEach((row, i) => {
        html += `<tr><th style="color: #90e0ef;">${alternatives[i]}</th>`;
        row.forEach((cell, j) => {
            const cellClass = cell === 1 ? 'matrix-cell-1' : 'matrix-cell-0';
            html += `<td class="${cellClass}">${cell}</td>`;
        });
        html += '</tr>';
    });
    html += '</table></div></div>';
    
    html += `
        <div>
            <div class="matrix-title">
                <span class="section-icon">⚖️</span>
                Матрица весов C (значения превосходства)
            </div>
            <div class="table-wrapper">
                <table class="data-grid">
                    <tr><th></th>
    `;
    
    alternatives.forEach(alt => {
        html += `<th>${alt}</th>`;
    });
    html += '</tr>';
    
    weightMatrix.forEach((row, i) => {
        html += `<tr><th style="color: #90e0ef;">${alternatives[i]}</th>`;
        row.forEach(cell => {
            const color = cell > 0 ? '#4361ee' : '#95a5a6';
            const bgColor = cell > 0 ? 'rgba(67, 97, 238, 0.1)' : 'transparent';
            html += `<td style="color: ${color}; font-weight: ${cell > 0 ? 'bold' : 'normal'}; background: ${bgColor};">${cell.toFixed(3)}</td>`;
        });
        html += '</tr>';
    });
    html += '</table></div></div>';
    
    document.getElementById('adjacency-matrix').innerHTML = html;
}

function calculateRankings(weightMatrix) {
    const n = alternatives.length;
    const indices = [];
    
    for (let j = 0; j < n; j++) {
        let incoming = 0;
        let outgoing = 0;
        
        for (let i = 0; i < n; i++) {
            incoming += weightMatrix[i][j];
            outgoing += weightMatrix[j][i];
        }
        
        indices.push({
            alternative: alternatives[j],
            index: incoming - outgoing,
            normalized: 0
        });
    }
    
    indices.sort((a, b) => b.index - a.index);
    
    const maxIndex = Math.max(...indices.map(item => item.index));
    const minIndex = Math.min(...indices.map(item => item.index));
    
    indices.forEach(item => {
        if (maxIndex !== minIndex) {
            item.normalized = (item.index - minIndex) / (maxIndex - minIndex);
        } else {
            item.normalized = 0.5;
        }
    });
    
    return indices;
}

function displayRankings(rankings) {
    let html = '';
    
    rankings.forEach((item, idx) => {
        html += `
            <tr>
                <td class="place-cell">${idx + 1}</td>
                <td class="alternative-cell">${item.alternative}</td>
                <td class="index-cell">${item.index.toFixed(4)}</td>
                <td class="norm-cell">${item.normalized.toFixed(4)}</td>
            </tr>
        `;
    });
    
    document.getElementById('ranking-table-body').innerHTML = html;
}

function drawChart(rankings) {
    const ctx = document.getElementById('resultsChart').getContext('2d');
    
    if (resultsChart !== null) {
        resultsChart.destroy();
    }
    
    const labels = rankings.map(item => item.alternative);
    const data = rankings.map(item => item.normalized);
    
    resultsChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Нормированная оценка',
                data: data,
                backgroundColor: [
                    'rgba(0, 180, 216, 0.7)',
                    'rgba(67, 97, 238, 0.7)',
                    'rgba(46, 204, 113, 0.7)',
                    'rgba(157, 78, 221, 0.7)'
                ],
                borderColor: [
                    'rgba(0, 180, 216, 1)',
                    'rgba(67, 97, 238, 1)',
                    'rgba(46, 204, 113, 1)',
                    'rgba(157, 78, 221, 1)'
                ],
                borderWidth: 2,
                borderRadius: 6,
                borderSkipped: false,
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            return `Оценка: ${context.parsed.y.toFixed(4)}`;
                        }
                    }
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    max: 1,
                    grid: {
                        color: 'rgba(255, 255, 255, 0.1)'
                    },
                    ticks: {
                        color: '#8ecae6',
                        font: {
                            size: 11
                        }
                    },
                    title: {
                        display: true,
                        text: 'Нормированная оценка',
                        color: '#90e0ef',
                        font: {
                            size: 12,
                            weight: 'bold'
                        }
                    }
                },
                x: {
                    grid: {
                        display: false
                    },
                    ticks: {
                        color: '#90e0ef',
                        font: {
                            size: 12,
                            weight: 'bold'
                        }
                    },
                    title: {
                        display: true,
                        text: 'Альтернативы',
                        color: '#90e0ef',
                        font: {
                            size: 12,
                            weight: 'bold'
                        }
                    }
                }
            }
        }
    });
}

function showLPRDialog() {
    if (currentRankings && currentRankings.length > 0) {
        const bestAlternative = currentRankings[0].alternative;
        document.getElementById('recommended-alternative').textContent = bestAlternative;
        document.getElementById('lpr-dialog').style.display = 'flex';
    }
}

function agreeWithRecommendation() {
    const bestAlternative = currentRankings[0].alternative;
    document.getElementById('final-decision-text').textContent = bestAlternative;
    document.getElementById('lpr-dialog').style.display = 'none';
    document.getElementById('final-dialog').style.display = 'flex';
    showNotification(`✅ Решение об инвестировании: ${bestAlternative}`);
}

function disagreeWithRecommendation() {
    document.getElementById('lpr-dialog').style.display = 'none';
    showAlternativeChoiceDialog();
}

function showAlternativeChoiceDialog() {
    let choicesHtml = '<div style="display: flex; flex-direction: column; gap: 15px;">';
    
    currentRankings.forEach((item, idx) => {
        choicesHtml += `
            <button class="action-btn" onclick="selectAlternative('${item.alternative}')"
                    style="justify-content: space-between;">
                <span>${item.alternative}</span>
                <span style="background: rgba(255, 255, 255, 0.2); padding: 5px 15px; border-radius: 20px;">
                    ${item.normalized.toFixed(4)}
                </span>
            </button>
        `;
    });
    
    choicesHtml += '</div>';
    document.getElementById('alternative-choices').innerHTML = choicesHtml;
    document.getElementById('choice-dialog').style.display = 'flex';
}

function selectAlternative(choice) {
    document.getElementById('final-decision-text').textContent = choice;
    document.getElementById('choice-dialog').style.display = 'none';
    document.getElementById('final-dialog').style.display = 'flex';
    showNotification(`✅ Выбран проект для инвестиций: ${choice}`);
}

function closeFinalDialog() {
    document.getElementById('final-dialog').style.display = 'none';
}

function showNotification(message) {
    const notification = document.getElementById('notification');
    const text = document.getElementById('notification-text');
    
    text.textContent = message;
    notification.style.display = 'block';
    
    setTimeout(() => {
        notification.style.display = 'none';
    }, 3000);
}

window.onload = function() {
    setupCriteria();
    setTimeout(() => {
        setupAlternatives();
    }, 100);
};
