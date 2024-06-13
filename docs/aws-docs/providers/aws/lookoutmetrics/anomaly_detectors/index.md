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

Creates, updates, deletes or gets an <code>anomaly_detector</code> resource or lists <code>anomaly_detectors</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>anomaly_detectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An Amazon Lookout for Metrics Detector</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lookoutmetrics.anomaly_detectors" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="anomaly_detector_name" /></td><td><code>string</code></td><td>Name for the Amazon Lookout for Metrics Anomaly Detector</td></tr>
<tr><td><CopyableCode code="anomaly_detector_description" /></td><td><code>string</code></td><td>A description for the AnomalyDetector.</td></tr>
<tr><td><CopyableCode code="anomaly_detector_config" /></td><td><code>object</code></td><td>Configuration options for the AnomalyDetector</td></tr>
<tr><td><CopyableCode code="metric_set_list" /></td><td><code>array</code></td><td>List of metric sets for anomaly detection</td></tr>
<tr><td><CopyableCode code="kms_key_arn" /></td><td><code>string</code></td><td>KMS key used to encrypt the AnomalyDetector data</td></tr>
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
    <td><CopyableCode code="AnomalyDetectorConfig, MetricSetList, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
List all <code>anomaly_detectors</code> in a region.
```sql
SELECT
region,
arn
FROM aws.lookoutmetrics.anomaly_detectors
WHERE region = 'us-east-1';
```
Gets all properties from an <code>anomaly_detector</code>.
```sql
SELECT
region,
arn,
anomaly_detector_name,
anomaly_detector_description,
anomaly_detector_config,
metric_set_list,
kms_key_arn
FROM aws.lookoutmetrics.anomaly_detectors
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```


## `INSERT` example

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
/*+ create */
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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
lookoutmetrics:DescribeAnomalyDetector,
lookoutmetrics:DescribeMetricSet,
lookoutmetrics:ListMetricSets
```

### Update
```json
lookoutmetrics:UpdateAnomalyDetector,
lookoutmetrics:UpdateMetricSet
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

