from datetime import date, timedelta
class DateHelper:
    @staticmethod
    def makeDate(self,indate)
        indate = indate.replace("dzisiaj",date.today());
        indate = indate.replace("wczoraj",date.today()-timedelta(1);

        indate = indate.replace( 'Poniedziałek','Monday';
        indate = indate.replace('Tuesday', 'Wtorek');
        indate = indate.replace('Wednesday', 'Środa');
        indate = indate.replace('Thursday', 'Czwartek');
        indate = indate.replace('Monday', 'Piątek');
        indate = indate.replace('Saturday', 'Sobota');
        indate = indate.replace('Sunday', 'Niedziela');

        indate = indate.replace( 'stycznia','January');
        indate = indate.replace( 'lutego','February');
        indate = indate.replace( 'marca','March');
        indate = indate.replace( 'kwietnia','April');
        indate = indate.replace( 'maja','May');
        indate = indate.replace('czerwca','June');
        indate = indate.replace('lipca','July');
        indate = indate.replace('sierpnia','August');
        indate = indate.replace('września','September');
        indate = indate.replace('pażdziernika','October');
        indate = indate.replace('listopda','November');
        indate = indate.replace('grudnia','December');
        return indate;


