import sys
sys.path.append('..')
from helpers import load_data_in_chunks, load_model, report_results

(Xs, Ys) = load_data_in_chunks('test', chunk_size=5)
Xs = Xs.astype('float32')
Ys = Ys.astype('float32')
regr = load_model('convolutional')
Ys_pred = regr.predict(Xs)
(a, b, c) = Xs.shape
report_results(Xs.reshape(a*b, c), Ys, Ys_pred, 'convolutional', 'convolutional.svg')
