---
title: table_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - table_tags
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Expands all tag keys and values for <code>tables</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>table_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::DynamoDB::Table</code> resource creates a DDB table. For more information, see &#91;CreateTable&#93;(https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_CreateTable.html) in the *API Reference*.<br />You should be aware of the following behaviors when working with DDB tables:<br />+ CFNlong typically creates DDB tables in parallel. However, if your template includes multiple DDB tables with indexes, you must declare dependencies so that the tables are created sequentially. DDBlong limits the number of tables with secondary indexes that are in the creating state. If you create multiple tables with indexes at the same time, DDB returns an error and the stack operation fails. For an example, see &#91;DynamoDB Table with a DependsOn Attribute&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#aws-resource-dynamodb-table--examples--DynamoDB_Table_with_a_DependsOn_Attribute).<br /><br />Our guidance is to use the latest schema documented for your CFNlong templates. This schema supports the provisioning of all table settings below. When using this schema in your CFNlong templates, please ensure that your Identity and Access Management (IAM) policies are updated with appropriate permissions to allow for the authorization of these setting changes.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.dynamodb.table_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="on_demand_throughput" /></td><td><code>object</code></td><td>Sets the maximum number of read and write units for the specified on-demand table. If you use this property, you must specify <code>MaxReadRequestUnits</code>, <code>MaxWriteRequestUnits</code>, or both.</td></tr>
<tr><td><CopyableCode code="sse_specification" /></td><td><code>object</code></td><td>Specifies the settings to enable server-side encryption.</td></tr>
<tr><td><CopyableCode code="kinesis_stream_specification" /></td><td><code>object</code></td><td>The Kinesis Data Streams configuration for the specified table.</td></tr>
<tr><td><CopyableCode code="stream_specification" /></td><td><code>object</code></td><td>The settings for the DDB table stream, which capture changes to items stored in the table.</td></tr>
<tr><td><CopyableCode code="contributor_insights_specification" /></td><td><code>object</code></td><td>The settings used to enable or disable CloudWatch Contributor Insights for the specified table.</td></tr>
<tr><td><CopyableCode code="import_source_specification" /></td><td><code>object</code></td><td>Specifies the properties of data being imported from the S3 bucket source to the" table.<br />If you specify the <code>ImportSourceSpecification</code> property, and also specify either the <code>StreamSpecification</code>, the <code>TableClass</code> property, the <code>DeletionProtectionEnabled</code> property, or the <code>WarmThroughput</code> property, the IAM entity creating/updating stack must have <code>UpdateTable</code> permission.</td></tr>
<tr><td><CopyableCode code="point_in_time_recovery_specification" /></td><td><code>object</code></td><td>The settings used to enable point in time recovery.</td></tr>
<tr><td><CopyableCode code="provisioned_throughput" /></td><td><code>object</code></td><td>Throughput for the specified table, which consists of values for <code>ReadCapacityUnits</code> and <code>WriteCapacityUnits</code>. For more information about the contents of a provisioned throughput structure, see &#91;Amazon DynamoDB Table ProvisionedThroughput&#93;(https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ProvisionedThroughput.html). <br />If you set <code>BillingMode</code> as <code>PROVISIONED</code>, you must specify this property. If you set <code>BillingMode</code> as <code>PAY_PER_REQUEST</code>, you cannot specify this property.</td></tr>
<tr><td><CopyableCode code="warm_throughput" /></td><td><code>object</code></td><td>Represents the warm throughput (in read units per second and write units per second) for creating a table.</td></tr>
<tr><td><CopyableCode code="table_name" /></td><td><code>string</code></td><td>A name for the table. If you don't specify a name, CFNlong generates a unique physical ID and uses that ID for the table name. For more information, see &#91;Name Type&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html).<br />If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.</td></tr>
<tr><td><CopyableCode code="attribute_definitions" /></td><td><code>array</code></td><td>A list of attributes that describe the key schema for the table and indexes.<br />This property is required to create a DDB table.<br />Update requires: &#91;Some interruptions&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt). Replacement if you edit an existing AttributeDefinition.</td></tr>
<tr><td><CopyableCode code="billing_mode" /></td><td><code>string</code></td><td>Specify how you are charged for read and write throughput and how you manage capacity.<br />Valid values include:<br />+ <code>PROVISIONED</code> - We recommend using <code>PROVISIONED</code> for predictable workloads. <code>PROVISIONED</code> sets the billing mode to &#91;Provisioned Mode&#93;(https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadWriteCapacityMode.html#HowItWorks.ProvisionedThroughput.Manual).<br />+ <code>PAY_PER_REQUEST</code> - We recommend using <code>PAY_PER_REQUEST</code> for unpredictable workloads. <code>PAY_PER_REQUEST</code> sets the billing mode to &#91;On-Demand Mode&#93;(https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadWriteCapacityMode.html#HowItWorks.OnDemand).<br /><br />If not specified, the default is <code>PROVISIONED</code>.</td></tr>
<tr><td><CopyableCode code="global_secondary_indexes" /></td><td><code>array</code></td><td>Global secondary indexes to be created on the table. You can create up to 20 global secondary indexes.<br />If you update a table to include a new global secondary index, CFNlong initiates the index creation and then proceeds with the stack update. CFNlong doesn't wait for the index to complete creation because the backfilling phase can take a long time, depending on the size of the table. You can't use the index or update the table until the index's status is <code>ACTIVE</code>. You can track its status by using the DynamoDB &#91;DescribeTable&#93;(https://docs.aws.amazon.com/cli/latest/reference/dynamodb/describe-table.html) command.<br />If you add or delete an index during an update, we recommend that you don't update any other resources. If your stack fails to update and is rolled back while adding a new index, you must manually delete the index. <br />Updates are not supported. The following are exceptions:<br />+ If you update either the contributor insights specification or the provisioned throughput values of global secondary indexes, you can update the table without interruption.<br />+ You can delete or add one global secondary index without interruption. If you do both in the same update (for example, by changing the index's logical ID), the update fails.</td></tr>
<tr><td><CopyableCode code="resource_policy" /></td><td><code>object</code></td><td>A resource-based policy document that contains permissions to add to the specified table. In a CFNshort template, you can provide the policy in JSON or YAML format because CFNshort converts YAML to JSON before submitting it to DDB. For more information about resource-based policies, see &#91;Using resource-based policies for&#93;(https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/access-control-resource-based.html) and &#91;Resource-based policy examples&#93;(https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/rbac-examples.html).<br />When you attach a resource-based policy while creating a table, the policy creation is *strongly consistent*. For information about the considerations that you should keep in mind while attaching a resource-based policy, see &#91;Resource-based policy considerations&#93;(https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/rbac-considerations.html).</td></tr>
<tr><td><CopyableCode code="key_schema" /></td><td><code></code></td><td>Specifies the attributes that make up the primary key for the table. The attributes in the <code>KeySchema</code> property must also be defined in the <code>AttributeDefinitions</code> property.</td></tr>
<tr><td><CopyableCode code="local_secondary_indexes" /></td><td><code>array</code></td><td>Local secondary indexes to be created on the table. You can create up to 5 local secondary indexes. Each index is scoped to a given hash key value. The size of each hash key can be up to 10 gigabytes.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="stream_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="deletion_protection_enabled" /></td><td><code>boolean</code></td><td>Determines if a table is protected from deletion. When enabled, the table cannot be deleted by any user or process. This setting is disabled by default. For more information, see &#91;Using deletion protection&#93;(https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithTables.Basics.html#WorkingWithTables.Basics.DeletionProtection) in the *Developer Guide*.</td></tr>
<tr><td><CopyableCode code="table_class" /></td><td><code>string</code></td><td>The table class of the new table. Valid values are <code>STANDARD</code> and <code>STANDARD_INFREQUENT_ACCESS</code>.</td></tr>
<tr><td><CopyableCode code="time_to_live_specification" /></td><td><code>object</code></td><td>Specifies the Time to Live (TTL) settings for the table.<br />For detailed information about the limits in DynamoDB, see &#91;Limits in Amazon DynamoDB&#93;(https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html) in the Amazon DynamoDB Developer Guide.</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Expands tags for all <code>tables</code> in a region.
```sql
SELECT
region,
on_demand_throughput,
sse_specification,
kinesis_stream_specification,
stream_specification,
contributor_insights_specification,
import_source_specification,
point_in_time_recovery_specification,
provisioned_throughput,
warm_throughput,
table_name,
attribute_definitions,
billing_mode,
global_secondary_indexes,
resource_policy,
key_schema,
local_secondary_indexes,
arn,
stream_arn,
deletion_protection_enabled,
table_class,
time_to_live_specification,
tag_key,
tag_value
FROM aws.dynamodb.table_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>table_tags</code> resource, see <a href="/providers/aws/dynamodb/tables/#permissions"><code>tables</code></a>

