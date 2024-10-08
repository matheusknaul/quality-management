from configuration import pc_casa_gecko, pc_casa_firefox, pc_trabalho_gecko, pc_trabalho_firefox
import configuration

service = Service(executable_path = pc_trabalho_gecko)
options = Options()
options.binary_location = pc_trabalho_firefox
driver = webdriver.Firefox(service=service, options=options)