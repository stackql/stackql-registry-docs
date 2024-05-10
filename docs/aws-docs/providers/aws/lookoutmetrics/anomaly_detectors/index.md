---
title: anomaly_detectors
hide_title: false
hide_table_of_contents: false
keywords:
  - anomaly_detectors
  - lookoutmetrics
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Used to retrieve a list of <code>anomaly_detectors</code> in a region or to create or delete a <code>anomaly_detectors</code> resource, use <code>anomaly_detector</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>anomaly_detectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An Amazon Lookout for Metrics Detector</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lookoutmetrics.anomaly_detectors" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
arn
FROM aws.lookoutmetrics.anomaly_detectors
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>anomaly_detector</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
-- anomaly_detector.iql (required properties only)
INSERT INTO aws.lookoutmetrics.anomaly_detectors (
 AnomalyDetectorConfig,
 MetricSetList,
 region
)
SELECT 
'{{ AnomalyDetectorConfig }}',
 '{{ MetricSetList }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- anomaly_detector.iql (all properties)
INSERT INTO aws.lookoutmetrics.anomaly_detectors (
 AnomalyDetectorName,
 AnomalyDetectorDescription,
 AnomalyDetectorConfig,
 MetricSetList,
 KmsKeyArn,
 region
)
SELECT 
 '{{ AnomalyDetectorName }}',
 '{{ AnomalyDetectorDescription }}',
 '{{ AnomalyDetectorConfig }}',
 '{{ MetricSetList }}',
 '{{ KmsKeyArn }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: anomaly_detector
    props:
      - name: AnomalyDetectorName
        value: '{{ AnomalyDetectorName }}'
      - name: AnomalyDetectorDescription
        value: '{{ AnomalyDetectorDescription }}'
      - name: AnomalyDetectorConfig
        value:
          AnomalyDetectorFrequency: '{{ AnomalyDetectorFrequency }}'
      - name: MetricSetList
        value:
          - MetricSetName: '{{ MetricSetName }}'
            MetricSetDescription: '{{ MetricSetDescription }}'
            MetricSource:
              S3SourceConfig:
                RoleArn: '{{ RoleArn }}'
                TemplatedPathList:
                  - '{{ TemplatedPathList[0] }}'
                HistoricalDataPathList:
                  - '{{ HistoricalDataPathList[0] }}'
                FileFormatDescriptor:
                  CsvFormatDescriptor:
                    FileCompression: '{{ FileCompression }}'
                    Charset: '{{ Charset }}'
                    Delimiter: '{{ Delimiter }}'
                    HeaderList:
                      - '{{ HeaderList[0] }}'
                    QuoteSymbol: '{{ QuoteSymbol }}'
                    ContainsHeader: '{{ ContainsHeader }}'
                  JsonFormatDescriptor:
                    FileCompression: '{{ FileCompression }}'
                    Charset: null
              RDSSourceConfig:
                DBInstanceIdentifier: '{{ DBInstanceIdentifier }}'
                DatabaseHost: '{{ DatabaseHost }}'
                DatabasePort: '{{ DatabasePort }}'
                SecretManagerArn: '{{ SecretManagerArn }}'
                DatabaseName: '{{ DatabaseName }}'
                TableName: '{{ TableName }}'
                RoleArn: null
                VpcConfiguration:
                  SubnetIdList:
                    - '{{ SubnetIdList[0] }}'
                  SecurityGroupIdList:
                    - '{{ SecurityGroupIdList[0] }}'
              RedshiftSourceConfig:
                ClusterIdentifier: '{{ ClusterIdentifier }}'
                DatabaseHost: null
                DatabasePort: null
                SecretManagerArn: null
                DatabaseName: '{{ DatabaseName }}'
                TableName: null
                RoleArn: null
                VpcConfiguration: null
              CloudwatchConfig:
                RoleArn: null
              AppFlowConfig:
                RoleArn: null
                FlowName: '{{ FlowName }}'
            MetricList:
              - MetricName: null
                AggregationFunction: '{{ AggregationFunction }}'
                Namespace: '{{ Namespace }}'
            Offset: '{{ Offset }}'
            TimestampColumn:
              ColumnName: null
              ColumnFormat: '{{ ColumnFormat }}'
            DimensionList:
              - null
            MetricSetFrequency: '{{ MetricSetFrequency }}'
            Timezone: '{{ Timezone }}'
      - name: KmsKeyArn
        value: '{{ KmsKeyArn }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.lookoutmetrics.anomaly_detectors
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>anomaly_detectors</code> resource, the following permissions are required:

### Create
```json
lookoutmetrics:CreateAnomalyDetector,
lookoutmetrics:DeleteAnomalyDetector,
lookoutmetrics:CreateMetricSet,
iam:PassRole
```

### Delete
```json
lookoutmetrics:DescribeAnomalyDetector,
lookoutmetrics:DeleteAnomalyDetector
```

### List
```json
lookoutmetrics:ListAnomalyDetectors
```

