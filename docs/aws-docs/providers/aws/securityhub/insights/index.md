---
title: insights
hide_title: false
hide_table_of_contents: false
keywords:
  - insights
  - securityhub
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

Creates, updates, deletes or gets an <code>insight</code> resource or lists <code>insights</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>insights</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::SecurityHub::Insight resource represents the AWS Security Hub Insight in your account. An AWS Security Hub insight is a collection of related findings.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.securityhub.insights" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="insight_arn" /></td><td><code>string</code></td><td>The ARN of a Security Hub insight</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of a Security Hub insight</td></tr>
<tr><td><CopyableCode code="filters" /></td><td><code>object</code></td><td>One or more attributes used to filter the findings included in the insight</td></tr>
<tr><td><CopyableCode code="group_by_attribute" /></td><td><code>string</code></td><td>The grouping attribute for the insight's findings</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-insight.html"><code>AWS::SecurityHub::Insight</code></a>.

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
    <td><CopyableCode code="Filters, Name, GroupByAttribute, region" /></td>
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
    <td><CopyableCode code="list_resources" /></td>
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
Gets all <code>insights</code> in a region.
```sql
SELECT
region,
insight_arn,
name,
filters,
group_by_attribute
FROM aws.securityhub.insights
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>insight</code>.
```sql
SELECT
region,
insight_arn,
name,
filters,
group_by_attribute
FROM aws.securityhub.insights
WHERE region = 'us-east-1' AND data__Identifier = '<InsightArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>insight</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.securityhub.insights (
 Name,
 Filters,
 GroupByAttribute,
 region
)
SELECT 
'{{ Name }}',
 '{{ Filters }}',
 '{{ GroupByAttribute }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.securityhub.insights (
 Name,
 Filters,
 GroupByAttribute,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Filters }}',
 '{{ GroupByAttribute }}',
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
  - name: insight
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Filters
        value:
          ProductArn:
            - Comparison: '{{ Comparison }}'
              Value: '{{ Value }}'
          AwsAccountId:
            - null
          AwsAccountName:
            - null
          Id:
            - null
          GeneratorId:
            - null
          Type:
            - null
          Region:
            - null
          FirstObservedAt:
            - DateRange:
                Unit: '{{ Unit }}'
                Value: null
              End: '{{ End }}'
              Start: null
          LastObservedAt:
            - null
          CreatedAt:
            - null
          UpdatedAt:
            - null
          SeverityLabel:
            - null
          Confidence:
            - Eq: null
              Gte: null
              Lte: null
          Criticality:
            - null
          Title:
            - null
          Description:
            - null
          RecommendationText:
            - null
          SourceUrl:
            - null
          ProductFields:
            - Comparison: '{{ Comparison }}'
              Key: null
              Value: null
          ProductName:
            - null
          CompanyName:
            - null
          UserDefinedFields:
            - null
          MalwareName:
            - null
          MalwareType:
            - null
          MalwarePath:
            - null
          MalwareState:
            - null
          NetworkDirection:
            - null
          NetworkProtocol:
            - null
          NetworkSourceIpV4:
            - Cidr: null
          NetworkSourceIpV6:
            - null
          NetworkSourcePort:
            - null
          NetworkSourceDomain:
            - null
          NetworkSourceMac:
            - null
          NetworkDestinationIpV4:
            - null
          NetworkDestinationIpV6:
            - null
          NetworkDestinationPort:
            - null
          NetworkDestinationDomain:
            - null
          ProcessName:
            - null
          ProcessPath:
            - null
          ProcessPid:
            - null
          ProcessParentPid:
            - null
          ProcessLaunchedAt:
            - null
          ProcessTerminatedAt:
            - null
          ThreatIntelIndicatorType:
            - null
          ThreatIntelIndicatorValue:
            - null
          ThreatIntelIndicatorCategory:
            - null
          ThreatIntelIndicatorLastObservedAt:
            - null
          ThreatIntelIndicatorSource:
            - null
          ThreatIntelIndicatorSourceUrl:
            - null
          ResourceType:
            - null
          ResourceId:
            - null
          ResourcePartition:
            - null
          ResourceRegion:
            - null
          ResourceTags:
            - null
          ResourceAwsEc2InstanceType:
            - null
          ResourceAwsEc2InstanceImageId:
            - null
          ResourceAwsEc2InstanceIpV4Addresses:
            - null
          ResourceAwsEc2InstanceIpV6Addresses:
            - null
          ResourceAwsEc2InstanceKeyName:
            - null
          ResourceAwsEc2InstanceIamInstanceProfileArn:
            - null
          ResourceAwsEc2InstanceVpcId:
            - null
          ResourceAwsEc2InstanceSubnetId:
            - null
          ResourceAwsEc2InstanceLaunchedAt:
            - null
          ResourceAwsS3BucketOwnerId:
            - null
          ResourceAwsS3BucketOwnerName:
            - null
          ResourceAwsIamAccessKeyStatus:
            - null
          ResourceAwsIamAccessKeyCreatedAt:
            - null
          ResourceContainerName:
            - null
          ResourceContainerImageId:
            - null
          ResourceContainerImageName:
            - null
          ResourceContainerLaunchedAt:
            - null
          ResourceDetailsOther:
            - null
          ComplianceStatus:
            - null
          VerificationState:
            - null
          WorkflowState:
            - null
          WorkflowStatus:
            - null
          RecordState:
            - null
          RelatedFindingsProductArn:
            - null
          RelatedFindingsId:
            - null
          ResourceApplicationArn:
            - null
          ResourceApplicationName:
            - null
          NoteText:
            - null
          NoteUpdatedAt:
            - null
          NoteUpdatedBy:
            - null
          Sample:
            - Value: '{{ Value }}'
          ComplianceAssociatedStandardsId:
            - null
          ComplianceSecurityControlId:
            - null
          ComplianceSecurityControlParametersName:
            - null
          ComplianceSecurityControlParametersValue:
            - null
          FindingProviderFieldsConfidence:
            - null
          FindingProviderFieldsCriticality:
            - null
          FindingProviderFieldsRelatedFindingsId:
            - null
          FindingProviderFieldsRelatedFindingsProductArn:
            - null
          FindingProviderFieldsSeverityLabel:
            - null
          FindingProviderFieldsSeverityOriginal:
            - null
          FindingProviderFieldsTypes:
            - null
          ResourceAwsIamAccessKeyPrincipalName:
            - null
          ResourceAwsIamUserUserName:
            - null
          VulnerabilitiesExploitAvailable:
            - null
          VulnerabilitiesFixAvailable:
            - null
          Keyword:
            - Value: null
          ResourceAwsIamAccessKeyUserName:
            - null
          SeverityNormalized:
            - null
          SeverityProduct:
            - null
      - name: GroupByAttribute
        value: null

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.securityhub.insights
WHERE data__Identifier = '<InsightArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>insights</code> resource, the following permissions are required:

### Create
```json
securityhub:CreateInsight
```

### Read
```json
securityhub:GetInsights
```

### Update
```json
securityhub:UpdateInsight
```

### Delete
```json
securityhub:GetInsights,
securityhub:DeleteInsight
```

### List
```json
securityhub:GetInsights
```
