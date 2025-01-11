---
title: db_instances_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - db_instances_list_only
  - rds
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

Lists <code>db_instances</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/db_instances/"><code>db_instances</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_instances_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::RDS::DBInstance</code> resource creates an Amazon DB instance. The new DB instance can be an RDS DB instance, or it can be a DB instance in an Aurora DB cluster.<br />For more information about creating an RDS DB instance, see &#91;Creating an Amazon RDS DB instance&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateDBInstance.html) in the *Amazon RDS User Guide*.<br />For more information about creating a DB instance in an Aurora DB cluster, see &#91;Creating an Amazon Aurora DB cluster&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.CreateInstance.html) in the *Amazon Aurora User Guide*.<br />If you import an existing DB instance, and the template configuration doesn't match the actual configuration of the DB instance, AWS CloudFormation applies the changes in the template during the import operation.<br />If a DB instance is deleted or replaced during an update, AWS CloudFormation deletes all automated snapshots. However, it retains manual DB snapshots. During an update that requires replacement, you can apply a stack policy to prevent DB instances from being replaced. For more information, see &#91;Prevent Updates to Stack Resources&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/protect-stack-resources.html).<br />*Updating DB instances* <br />When properties labeled "*Update requires:* &#91;Replacement&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)" are updated, AWS CloudFormation first creates a replacement DB instance, then changes references from other dependent resources to point to the replacement DB instance, and finally deletes the old DB instance.<br />We highly recommend that you take a snapshot of the database before updating the stack. If you don't, you lose the data when AWS CloudFormation replaces your DB instance. To preserve your data, perform the following procedure:<br />1. Deactivate any applications that are using the DB instance so that there's no activity on the DB instance.<br />1. Create a snapshot of the DB instance. For more information, see &#91;Creating a DB Snapshot&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateSnapshot.html).<br />1. If you want to restore your instance using a DB snapshot, modify the updated template with your DB instance changes and add the <code>DBSnapshotIdentifier</code> property with the ID of the DB snapshot that you want to use.<br />After you restore a DB instance with a <code>DBSnapshotIdentifier</code> property, you can delete the <code>DBSnapshotIdentifier</code> property. When you specify this property for an update, the DB instance is not restored from the DB snapshot again, and the data in the database is not changed. However, if you don't specify the <code>DBSnapshotIdentifier</code> property, an empty DB instance is created, and the original DB instance is deleted. If you specify a property that is different from the previous snapshot restore property, a new DB instance is restored from the specified <code>DBSnapshotIdentifier</code> property, and the original DB instance is deleted.<br />1. Update the stack.<br /><br />For more information about updating other properties of this resource, see <code>ModifyDBInstance</code>. For more information about updating stacks, see &#91;CloudFormation Stacks Updates&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks.html).<br />*Deleting DB instances* <br />For DB instances that are part of an Aurora DB cluster, you can set a deletion policy for your DB instance to control how AWS CloudFormation handles the DB instance when the stack is deleted. For Amazon RDS DB instances, you can choose to *retain* the DB instance, to *delete* the DB instance, or to *create a snapshot* of the DB instance. The default AWS CloudFormation behavior depends on the <code>DBClusterIdentifier</code> property:<br />1. For <code>AWS::RDS::DBInstance</code> resources that don't specify the <code>DBClusterIdentifier</code> property, AWS CloudFormation saves a snapshot of the DB instance.<br />1. For <code>AWS::RDS::DBInstance</code> resources that do specify the <code>DBClusterIdentifier</code> property, AWS CloudFormation deletes the DB instance.<br /><br />For more information, see &#91;DeletionPolicy Attribute&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html).</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rds.db_instances_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="db_instance_identifier" /></td><td><code>string</code></td><td>A name for the DB instance. If you specify a name, AWS CloudFormation converts it to lowercase. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the DB instance. For more information, see &#91;Name Type&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html).<br />For information about constraints that apply to DB instance identifiers, see &#91;Naming constraints in Amazon RDS&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Limits.html#RDS_Limits.Constraints) in the *Amazon RDS User Guide*.<br />If you specify a name, you can't perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.</td></tr>
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
Lists all <code>db_instances</code> in a region.
```sql
SELECT
region,
db_instance_identifier
FROM aws.rds.db_instances_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>db_instances_list_only</code> resource, see <a href="/providers/aws/rds/db_instances/#permissions"><code>db_instances</code></a>

