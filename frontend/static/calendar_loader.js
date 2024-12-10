// calendar_loader.js

$(function() {
 $('#calendar').fullCalendar({
   defaultView: 'agendaWeek',
   header: {
     left: 'prev,next today',
     center: 'title',
     right: 'agendaWeek,agendaDay'
   },
   // тестовой файл: https://fullcalendar.io/docs/events-json-feed
   events: 'https://f7f2013c-d34e-4560-99c6-5a60b6d5b291.selstorage.ru/user_1/09.12.24-13.12.24.json'
 })
});