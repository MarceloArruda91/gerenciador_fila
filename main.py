from fila_normal import FilaNormal
from fila_prioritaria import FilaPrioritaria
from fabrica_fila import FabricaFila
from estatistica_resumida import EstatisticaResumida
from estatistica_detalhada import EstatisticaDetalhada



fila = FabricaFila.pega_fila('prioritaria')

print(fila.chama_cliente(2))
print(fila.estatistica(EstatisticaResumida('29/09/2021', 15)))
