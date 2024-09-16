document.addEventListener('DOMContentLoaded', function () {
    var container = document.getElementById('timeline');
    
    var groups = new vis.DataSet([
        {id: 1, content: 'Diseño', nestedGroups: [11, 12]},
        {id: 11, content: 'Empleado 1'},
        {id: 12, content: 'Empleado 2'},
        {id: 2, content: 'Desarrollo', nestedGroups: [21, 22]},
        {id: 21, content: 'Empleado 1'},
        {id: 22, content: 'Empleado 2'},
        {id: 3, content: 'Despliegue', nestedGroups: [31, 32]},
        {id: 31, content: 'Empleado 1'},
        {id: 32, content: 'Empleado 2'}
    ]);

    var items = new vis.DataSet([
        {id: 1, group: 11, content: 'Diseño de interfaz', start: '2024-01-01', end: '2024-02-15'},
        {id: 2, group: 12, content: 'Diseño de base de datos', start: '2024-01-15', end: '2024-03-01'},
        {id: 3, group: 21, content: 'Desarrollo de backend', start: '2024-03-01', end: '2024-05-15'},
        {id: 4, group: 22, content: 'Desarrollo de frontend', start: '2024-03-15', end: '2024-06-01'},
        {id: 5, group: 31, content: 'Configuración de servidor', start: '2024-06-01', end: '2024-07-15'},
        {id: 6, group: 32, content: 'Pruebas de integración', start: '2024-07-01', end: '2024-08-15'}
    ]);

    var options = {
        groupOrder: 'content',
        width: '100%',
        height: '400px',
        stack: true,
        showMajorLabels: true,
        showCurrentTime: false,
        zoomMin: 1000 * 60 * 60 * 24 * 31, // about a month
        zoomMax: 1000 * 60 * 60 * 24 * 366, // about a year
        orientation: 'top',
        start: new Date(2024, 0, 1),
        end: new Date(2024, 11, 31)
    };

    var timeline = new vis.Timeline(container, items, groups, options);
});