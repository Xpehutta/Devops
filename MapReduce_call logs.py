import pandas as pd
import numpy as np
from datetime import datetime

data = pd.read_csv('contacts', names = ['contact_id', 'client_id', 'employee_id','started_dttm', 'finished_dttm'
                                        , 'business_line', 'route_type', 'initiator_id'], sep = '\t')

data['started_dttm'] = pd.to_datetime(data['started_dttm'])
data['finished_dttm'] = pd.to_datetime(data['finished_dttm'])
data_emp = data[['employee_id', 'started_dttm', 'finished_dttm']].groupby('employee_id').agg(
    first_date=('started_dttm', np.min),
    last_date=('finished_dttm', np.max)).reset_index()
data_emp['work'] = (data_emp['last_date'] - data_emp['first_date']).dt.days

data = data[data['employee_id'].isin(data_emp[data_emp['work'] >= 180]['employee_id'].to_list())]
data = data[(data['business_line'].str.upper() == 'CREDIT CARD') & (data['route_type'].str.upper() == 'TELEPHONY')]
data['call'] = (data['finished_dttm'] - data['started_dttm']).dt.seconds
data['employee_id'] = data['employee_id'].astype('string')
data['initiator_id'] = data['initiator_id'].astype('string')
data["intiator"] = data["employee_id"] == data["initiator_id"]

filnal_data = pd.pivot_table(data, values='call', index=['employee_id'],
                 columns=['intiator'], aggfunc=np.mean).reset_index()

for i in filnal_data.values.tolist()[:10]:
  print("{0}\t{1}\t{2}".format(i[0], int(i[1]), int(i[2])))
