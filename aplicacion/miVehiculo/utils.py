def fechaLicencia(fechaInicial, tipoLicencia):
    """
    Este modulo se encarga de calcular la fecha de expiracion de la licencia
    """
    fechaExpiraLicencia = ""
    year = fechaInicial.year
    month = fechaInicial.month
    day = fechaInicial.day
    if month<10:
        month = "0"+str(month)
    if day<10:
        day="0"+str(day)
    if (tipoLicencia == 'A1' or tipoLicencia == 'A2'):
        fechaExpiraLicencia = str(year+1)+"-"+month+"-"+str(day)
    elif (tipoLicencia == 'B1' or tipoLicencia == 'B2'):
        fechaExpiraLicencia = str(year+1)+"-"+month+"-"+str(day)
    elif (tipoLicencia == 'C1' or tipoLicencia == 'C2'):
        fechaExpiraLicencia = str(year+3)+"-"+month+"-"+str(day)
    return fechaExpiraLicencia