---
title: table
hide_title: false
hide_table_of_contents: false
keywords:
  - table
  - dynamodb
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>table</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>table</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>table</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.dynamodb.table</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>s_se_specification</code></td><td><code>object</code></td><td>Specifies the settings to enable server-side encryption.</td></tr>
<tr><td><code>kinesis_stream_specification</code></td><td><code>object</code></td><td>The Kinesis Data Streams configuration for the specified table.</td></tr>
<tr><td><code>stream_specification</code></td><td><code>object</code></td><td>The settings for the DDB table stream, which capture changes to items stored in the table.</td></tr>
<tr><td><code>contributor_insights_specification</code></td><td><code>object</code></td><td>The settings used to enable or disable CloudWatch Contributor Insights for the specified table.</td></tr>
<tr><td><code>import_source_specification</code></td><td><code>object</code></td><td>Specifies the properties of data being imported from the S3 bucket source to the table.&lt;br&#x2F;&gt;  If you specify the ``ImportSourceSpecification`` property, and also specify either the ``StreamSpecification``, the ``TableClass`` property, or the ``DeletionProtectionEnabled`` property, the IAM entity creating&#x2F;updating stack must have ``UpdateTable`` permission.</td></tr>
<tr><td><code>point_in_time_recovery_specification</code></td><td><code>object</code></td><td>The settings used to enable point in time recovery.</td></tr>
<tr><td><code>provisioned_throughput</code></td><td><code>object</code></td><td>Throughput for the specified table, which consists of values for ``ReadCapacityUnits`` and ``WriteCapacityUnits``. For more information about the contents of a provisioned throughput structure, see &#91;Amazon DynamoDB Table ProvisionedThroughput&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;amazondynamodb&#x2F;latest&#x2F;APIReference&#x2F;API_ProvisionedThroughput.html). &lt;br&#x2F;&gt; If you set ``BillingMode`` as ``PROVISIONED``, you must specify this property. If you set ``BillingMode`` as ``PAY_PER_REQUEST``, you cannot specify this property.</td></tr>
<tr><td><code>table_name</code></td><td><code>string</code></td><td>A name for the table. If you don't specify a name, CFNlong generates a unique physical ID and uses that ID for the table name. For more information, see &#91;Name Type&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-properties-name.html).&lt;br&#x2F;&gt;  If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.</td></tr>
<tr><td><code>attribute_definitions</code></td><td><code>array</code></td><td>A list of attributes that describe the key schema for the table and indexes.&lt;br&#x2F;&gt; This property is required to create a DDB table.&lt;br&#x2F;&gt; Update requires: &#91;Some interruptions&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt). Replacement if you edit an existing AttributeDefinition.</td></tr>
<tr><td><code>billing_mode</code></td><td><code>string</code></td><td>Specify how you are charged for read and write throughput and how you manage capacity.&lt;br&#x2F;&gt; Valid values include:&lt;br&#x2F;&gt;  +   ``PROVISIONED`` - We recommend using ``PROVISIONED`` for predictable workloads. ``PROVISIONED`` sets the billing mode to &#91;Provisioned Mode&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;amazondynamodb&#x2F;latest&#x2F;developerguide&#x2F;HowItWorks.ReadWriteCapacityMode.html#HowItWorks.ProvisionedThroughput.Manual).&lt;br&#x2F;&gt;  +   ``PAY_PER_REQUEST`` - We recommend using ``PAY_PER_REQUEST`` for unpredictable workloads. ``PAY_PER_REQUEST`` sets the billing mode to &#91;On-Demand Mode&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;amazondynamodb&#x2F;latest&#x2F;developerguide&#x2F;HowItWorks.ReadWriteCapacityMode.html#HowItWorks.OnDemand).&lt;br&#x2F;&gt;  &lt;br&#x2F;&gt; If not specified, the default is ``PROVISIONED``.</td></tr>
<tr><td><code>global_secondary_indexes</code></td><td><code>array</code></td><td>Global secondary indexes to be created on the table. You can create up to 20 global secondary indexes.&lt;br&#x2F;&gt;  If you update a table to include a new global secondary index, CFNlong initiates the index creation and then proceeds with the stack update. CFNlong doesn't wait for the index to complete creation because the backfilling phase can take a long time, depending on the size of the table. You can't use the index or update the table until the index's status is ``ACTIVE``. You can track its status by using the DynamoDB &#91;DescribeTable&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;cli&#x2F;latest&#x2F;reference&#x2F;dynamodb&#x2F;describe-table.html) command.&lt;br&#x2F;&gt; If you add or delete an index during an update, we recommend that you don't update any other resources. If your stack fails to update and is rolled back while adding a new index, you must manually delete the index. &lt;br&#x2F;&gt; Updates are not supported. The following are exceptions:&lt;br&#x2F;&gt;  +  If you update either the contributor insights specification or the provisioned throughput value</td></tr>
<tr><td><code>key_schema</code></td><td><code>undefined</code></td><td>Specifies the attributes that make up the primary key for the table. The attributes in the ``KeySchema`` property must also be defined in the ``AttributeDefinitions`` property.</td></tr>
<tr><td><code>local_secondary_indexes</code></td><td><code>array</code></td><td>Local secondary indexes to be created on the table. You can create up to 5 local secondary indexes. Each index is scoped to a given hash key value. The size of each hash key can be up to 10 gigabytes.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>stream_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>deletion_protection_enabled</code></td><td><code>boolean</code></td><td>Determines if a table is protected from deletion. When enabled, the table cannot be deleted by any user or process. This setting is disabled by default. For more information, see &#91;Using deletion protection&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;amazondynamodb&#x2F;latest&#x2F;developerguide&#x2F;WorkingWithTables.Basics.html#WorkingWithTables.Basics.DeletionProtection) in the *Developer Guide*.</td></tr>
<tr><td><code>table_class</code></td><td><code>string</code></td><td>The table class of the new table. Valid values are ``STANDARD`` and ``STANDARD_INFREQUENT_ACCESS``.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.&lt;br&#x2F;&gt; For more information, see &#91;Tag&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-properties-resource-tags.html).</td></tr>
<tr><td><code>time_to_live_specification</code></td><td><code>object</code></td><td>Specifies the Time to Live (TTL) settings for the table.&lt;br&#x2F;&gt;  For detailed information about the limits in DynamoDB, see &#91;Limits in Amazon DynamoDB&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;amazondynamodb&#x2F;latest&#x2F;developerguide&#x2F;Limits.html) in the Amazon DynamoDB Developer Guide.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>table</code> resource, the following permissions are required:

### Read
```json
dynamodb:DescribeTable,
dynamodb:DescribeContinuousBackups,
dynamodb:DescribeContributorInsights,
dynamodb:DescribeKinesisStreamingDestination,
dynamodb:ListTagsOfResource,
dynamodb:GetResourcePolicy
```

### Update
```json
dynamodb:UpdateTable,
dynamodb:DescribeTable,
dynamodb:DescribeTimeToLive,
dynamodb:UpdateTimeToLive,
dynamodb:UpdateContinuousBackups,
dynamodb:UpdateContributorInsights,
dynamodb:UpdateKinesisStreamingDestination,
dynamodb:DescribeContinuousBackups,
dynamodb:DescribeKinesisStreamingDestination,
dynamodb:ListTagsOfResource,
dynamodb:TagResource,
dynamodb:UntagResource,
dynamodb:DescribeContributorInsights,
dynamodb:EnableKinesisStreamingDestination,
dynamodb:DisableKinesisStreamingDestination,
dynamodb:GetResourcePolicy,
dynamodb:PutResourcePolicy,
dynamodb:DeleteResourcePolicy,
kinesis:DescribeStream,
kinesis:PutRecords,
iam:CreateServiceLinkedRole,
kms:CreateGrant,
kms:DescribeKey,
kms:ListAliases,
kms:RevokeGrant
```

### Delete
```json
dynamodb:DeleteTable,
dynamodb:DescribeTable
```


## Example
```sql
SELECT
region,
s_se_specification,
kinesis_stream_specification,
stream_specification,
contributor_insights_specification,
import_source_specification,
point_in_time_recovery_specification,
provisioned_throughput,
table_name,
attribute_definitions,
billing_mode,
global_secondary_indexes,
key_schema,
local_secondary_indexes,
arn,
stream_arn,
deletion_protection_enabled,
table_class,
tags,
time_to_live_specification
FROM awscc.dynamodb.table
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;TableName&gt;'
```
