---
title: trails
hide_title: false
hide_table_of_contents: false
keywords:
  - trails
  - cloudtrail
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


Used to retrieve a list of <code>trails</code> in a region or to create or delete a <code>trails</code> resource, use <code>trail</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>trails</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates a trail that specifies the settings for delivery of log data to an Amazon S3 bucket. A maximum of five trails can exist in a region, irrespective of the region in which they were created.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudtrail.trails" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="trail_name" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="S3BucketName, IsLogging, region" /></td>
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
trail_name
FROM aws.cloudtrail.trails
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>trail</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.cloudtrail.trails (
 IsLogging,
 S3BucketName,
 region
)
SELECT 
'{{ IsLogging }}',
 '{{ S3BucketName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.cloudtrail.trails (
 CloudWatchLogsLogGroupArn,
 CloudWatchLogsRoleArn,
 EnableLogFileValidation,
 AdvancedEventSelectors,
 EventSelectors,
 IncludeGlobalServiceEvents,
 IsLogging,
 IsMultiRegionTrail,
 IsOrganizationTrail,
 KMSKeyId,
 S3BucketName,
 S3KeyPrefix,
 SnsTopicName,
 Tags,
 TrailName,
 InsightSelectors,
 region
)
SELECT 
 '{{ CloudWatchLogsLogGroupArn }}',
 '{{ CloudWatchLogsRoleArn }}',
 '{{ EnableLogFileValidation }}',
 '{{ AdvancedEventSelectors }}',
 '{{ EventSelectors }}',
 '{{ IncludeGlobalServiceEvents }}',
 '{{ IsLogging }}',
 '{{ IsMultiRegionTrail }}',
 '{{ IsOrganizationTrail }}',
 '{{ KMSKeyId }}',
 '{{ S3BucketName }}',
 '{{ S3KeyPrefix }}',
 '{{ SnsTopicName }}',
 '{{ Tags }}',
 '{{ TrailName }}',
 '{{ InsightSelectors }}',
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
  - name: trail
    props:
      - name: CloudWatchLogsLogGroupArn
        value: '{{ CloudWatchLogsLogGroupArn }}'
      - name: CloudWatchLogsRoleArn
        value: '{{ CloudWatchLogsRoleArn }}'
      - name: EnableLogFileValidation
        value: '{{ EnableLogFileValidation }}'
      - name: AdvancedEventSelectors
        value:
          - Name: '{{ Name }}'
            FieldSelectors:
              - Field: '{{ Field }}'
                Equals:
                  - '{{ Equals[0] }}'
                StartsWith:
                  - '{{ StartsWith[0] }}'
                EndsWith:
                  - '{{ EndsWith[0] }}'
                NotEquals:
                  - '{{ NotEquals[0] }}'
                NotStartsWith:
                  - '{{ NotStartsWith[0] }}'
                NotEndsWith:
                  - '{{ NotEndsWith[0] }}'
      - name: EventSelectors
        value:
          - DataResources:
              - Type: '{{ Type }}'
                Values:
                  - '{{ Values[0] }}'
            IncludeManagementEvents: '{{ IncludeManagementEvents }}'
            ReadWriteType: '{{ ReadWriteType }}'
            ExcludeManagementEventSources:
              - '{{ ExcludeManagementEventSources[0] }}'
      - name: IncludeGlobalServiceEvents
        value: '{{ IncludeGlobalServiceEvents }}'
      - name: IsLogging
        value: '{{ IsLogging }}'
      - name: IsMultiRegionTrail
        value: '{{ IsMultiRegionTrail }}'
      - name: IsOrganizationTrail
        value: '{{ IsOrganizationTrail }}'
      - name: KMSKeyId
        value: '{{ KMSKeyId }}'
      - name: S3BucketName
        value: '{{ S3BucketName }}'
      - name: S3KeyPrefix
        value: '{{ S3KeyPrefix }}'
      - name: SnsTopicName
        value: '{{ SnsTopicName }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: TrailName
        value: '{{ TrailName }}'
      - name: InsightSelectors
        value:
          - InsightType: '{{ InsightType }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
DELETE FROM aws.cloudtrail.trails
WHERE data__Identifier = '<TrailName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>trails</code> resource, the following permissions are required:

### Create
```json
CloudTrail:CreateTrail,
CloudTrail:StartLogging,
CloudTrail:AddTags,
CloudTrail:PutEventSelectors,
CloudTrail:PutInsightSelectors,
iam:GetRole,
iam:PassRole,
iam:CreateServiceLinkedRole,
organizations:DescribeOrganization,
organizations:ListAWSServiceAccessForOrganization
```

### Delete
```json
CloudTrail:DeleteTrail
```

### List
```json
CloudTrail:ListTrails,
CloudTrail:GetTrail,
CloudTrail:GetTrailStatus,
CloudTrail:ListTags,
CloudTrail:GetEventSelectors,
CloudTrail:GetInsightSelectors,
CloudTrail:DescribeTrails
```

