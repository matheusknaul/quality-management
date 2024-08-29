
class Range:
    def __init__(self, reference_value, read_value, uncertainty, uncertainty_percentage, critery, critery_percentage):
        self._vref = reference_value
        self._vi = read_value
        self._uncertainty = uncertainty
        self._uncertainty_percentage = uncertainty_percentage
        self._error = []
        self._total_error = []
        self._critery = critery
        self._validCritery = []
        self._critery_percentage = critery_percentage
        self._situation = []

        self.setError()
        self.setUncertainty()
        self.setTotalError()
        self.setValidCritery()
        self.setSituation()

        self.__str__()

    """Getters"""
    def getVi(self):
        return self._vi

    def getVref(self):
        return self._vref

    def getError(self):
        return self._error
    
    def getUncertainty(self):
        return self._uncertainty

    def getTotalError(self):
        return self._total_error
    
    def getCritery(self):
        return self._critery

    def getValidCritery(self):
        return self._validCritery

    def getSituation(self):
        return self._situation

    """Setters"""

    def setSituation(self):
        situation_new = []
        total_error = self.getTotalError()
        valid_critery = self.getValidCritery()

        for value in range(len(total_error)):
            if total_error[value] > valid_critery[value]:
                situation_new.append('Reprovado')
            else:
                situation_new.append('Aprovado')
        self._situation = situation_new

    def setValidCritery(self):
        validCritery_new = []
        critery = self.getCritery()
        vi = self.getVi()

        if self._critery_percentage:
            for value in range(len(critery)):
                validCritery_new.append((critery[value]/100) * vi[value])
            self._validCritery = validCritery_new
        else:
            for value in range(len(vi)):
                validCritery_new.append(critery)
            self._validCritery = validCritery_new

    def setUncertainty(self):
        uncertainty_new = []
        vi = self.getVi()
        uncertainty = self._uncertainty

        if self._uncertainty_percentage:
            for value in range(len(uncertainty)):
                uncertainty_new.append((uncertainty[value] / 100) * vi[value])
            self._uncertainty = uncertainty_new        

    def setError(self):
        error_new = []
        vi = self.getVi()
        vref = self.getVref()

        for value in range(len(vi)):
            error_new.append(vi[value] - vref[value])
        
        self._error = error_new
    
    def setTotalError(self):
        total_error_new = []
        error = self.getError()
        uncertainty = self.getUncertainty()

        for value in range(len(error)):
            total_error_new.append(abs(error[value]) + uncertainty[value])
        
        self._total_error = total_error_new
    
    """Methods"""

    def __str__(self):
        vi = self.getVi()
        vref = self.getVref()
        error = self.getError()
        uncertainty = self.getUncertainty()
        total_error = self.getTotalError()
        critery = self.getValidCritery()
        situation = self.getSituation()

        table = [
            ['Valor lido', 'Valor de Referência', 'Erro', 'Incerteza', 'Erro total', 'Critério', 'Situação']
        ]

        for value in range(len(vi)):
            table.append([vi[value], vref[value], error[value], uncertainty[value], total_error[value], critery[value], situation[value]])
        
        for x in table:
            print(x)


