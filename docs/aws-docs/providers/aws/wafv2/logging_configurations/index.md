---
title: logging_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - logging_configurations
  - wafv2
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

Creates, updates, deletes or gets a <code>logging_configuration</code> resource or lists <code>logging_configurations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>logging_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A WAFv2 Logging Configuration Resource Provider</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.wafv2.logging_configurations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="resource_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the web ACL that you want to associate with LogDestinationConfigs.</td></tr>
<tr><td><CopyableCode code="log_destination_configs" /></td><td><code>array</code></td><td>The Amazon Resource Names (ARNs) of the logging destinations that you want to associate with the web ACL.</td></tr>
<tr><td><CopyableCode code="redacted_fields" /></td><td><code>array</code></td><td>The parts of the request that you want to keep out of the logs. For example, if you redact the HEADER field, the HEADER field in the firehose will be xxx.</td></tr>
<tr><td><CopyableCode code="managed_by_firewall_manager" /></td><td><code>boolean</code></td><td>Indicates whether the logging configuration was created by AWS Firewall Manager, as part of an AWS WAF policy configuration. If true, only Firewall Manager can modify or delete the configuration.</td></tr>
<tr><td><CopyableCode code="logging_filter" /></td><td><code>object</code></td><td>Filtering that specifies which web requests are kept in the logs and which are dropped. You can filter on the rule action and on the web request labels that were applied by matching rules during web ACL evaluation.</td></tr>
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
    <td><CopyableCode code="ResourceArn, LogDestinationConfigs, region" /></td>
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
Gets all <code>logging_configurations</code> in a region.
```sql
SELECT
region,
resource_arn,
log_destination_configs,
redacted_fields,
managed_by_firewall_manager,
logging_filter
FROM aws.wafv2.logging_configurations
;
```
Gets all properties from an individual <code>logging_configuration</code>.
```sql
SELECT
region,
resource_arn,
log_destination_configs,
redacted_fields,
managed_by_firewall_manager,
logging_filter
FROM aws.wafv2.logging_configurations
WHERE data__Identifier = '<ResourceArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>logging_configuration</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.wafv2.logging_configurations (
 ResourceArn,
 LogDestinationConfigs,
 region
)
SELECT 
'{{ ResourceArn }}',
 '{{ LogDestinationConfigs }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.wafv2.logging_configurations (
 ResourceArn,
 LogDestinationConfigs,
 RedactedFields,
 LoggingFilter,
 region
)
SELECT 
 '{{ ResourceArn }}',
 '{{ LogDestinationConfigs }}',
 '{{ RedactedFields }}',
 '{{ LoggingFilter }}',
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
  - name: logging_configuration
    props:
      - name: ResourceArn
        value: '{{ ResourceArn }}'
      - name: LogDestinationConfigs
        value:
          - '{{ LogDestinationConfigs[0] }}'
      - name: RedactedFields
        value:
          - SingleHeader:
              Name: '{{ Name }}'
            SingleQueryArgument:
              Name: '{{ Name }}'
            AllQueryArguments: {}
            UriPath: {}
            QueryString: {}
            Body:
              OversizeHandling: '{{ OversizeHandling }}'
            Method: {}
            JsonBody:
              MatchPattern:
                All: {}
                IncludedPaths:
                  - '{{ IncludedPaths[0] }}'
              MatchScope: '{{ MatchScope }}'
              InvalidFallbackBehavior: '{{ InvalidFallbackBehavior }}'
              OversizeHandling: null
            Headers:
              MatchPattern:
                All: {}
                IncludedHeaders:
                  - '{{ IncludedHeaders[0] }}'
                ExcludedHeaders:
                  - '{{ ExcludedHeaders[0] }}'
              MatchScope: '{{ MatchScope }}'
              OversizeHandling: null
            Cookies:
              MatchPattern:
                All: {}
                IncludedCookies:
                  - '{{ IncludedCookies[0] }}'
                ExcludedCookies:
                  - '{{ ExcludedCookies[0] }}'
              MatchScope: null
              OversizeHandling: null
            JA3Fingerprint:
              FallbackBehavior: '{{ FallbackBehavior }}'
      - name: LoggingFilter
        value:
          DefaultBehavior: '{{ DefaultBehavior }}'
          Filters:
            - Behavior: '{{ Behavior }}'
              Conditions:
                - ActionCondition:
                    Action: '{{ Action }}'
                  LabelNameCondition:
                    LabelName: '{{ LabelName }}'
              Requirement: '{{ Requirement }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.wafv2.logging_configurations
WHERE data__Identifier = '<ResourceArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>logging_configurations</code> resource, the following permissions are required:

### Create
```json
wafv2:PutLoggingConfiguration,
wafv2:GetLoggingConfiguration,
firehose:ListDeliveryStreams,
iam:CreateServiceLinkedRole,
iam:DescribeOrganization,
logs:CreateLogDelivery,
s3:PutBucketPolicy,
s3:GetBucketPolicy,
logs:PutResourcePolicy,
logs:DescribeResourcePolicies,
logs:DescribeLogGroups
```

### Read
```json
wafv2:GetLoggingConfiguration
```

### Update
```json
wafv2:PutLoggingConfiguration,
wafv2:GetLoggingConfiguration,
firehose:ListDeliveryStreams,
iam:CreateServiceLinkedRole,
iam:DescribeOrganization,
logs:CreateLogDelivery,
s3:PutBucketPolicy,
s3:GetBucketPolicy,
logs:PutResourcePolicy,
logs:DescribeResourcePolicies,
logs:DescribeLogGroups
```

### Delete
```json
wafv2:DeleteLoggingConfiguration,
wafv2:GetLoggingConfiguration,
logs:DeleteLogDelivery
```

### List
```json
wafv2:ListLoggingConfigurations
```

