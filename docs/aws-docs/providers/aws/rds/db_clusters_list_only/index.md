---
title: db_clusters_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - db_clusters_list_only
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

Lists <code>db_clusters</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/db_clusters/"><code>db_clusters</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_clusters_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::RDS::DBCluster</code> resource creates an Amazon Aurora DB cluster or Multi-AZ DB cluster.<br />For more information about creating an Aurora DB cluster, see &#91;Creating an Amazon Aurora DB cluster&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.CreateInstance.html) in the *Amazon Aurora User Guide*.<br />For more information about creating a Multi-AZ DB cluster, see &#91;Creating a Multi-AZ DB cluster&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/create-multi-az-db-cluster.html) in the *Amazon RDS User Guide*.<br />You can only create this resource in AWS Regions where Amazon Aurora or Multi-AZ DB clusters are supported.<br />*Updating DB clusters* <br />When properties labeled "*Update requires:* &#91;Replacement&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)" are updated, AWS CloudFormation first creates a replacement DB cluster, then changes references from other dependent resources to point to the replacement DB cluster, and finally deletes the old DB cluster.<br />We highly recommend that you take a snapshot of the database before updating the stack. If you don't, you lose the data when AWS CloudFormation replaces your DB cluster. To preserve your data, perform the following procedure:<br />1. Deactivate any applications that are using the DB cluster so that there's no activity on the DB instance.<br />1. Create a snapshot of the DB cluster. For more information, see &#91;Creating a DB cluster snapshot&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_CreateSnapshotCluster.html).<br />1. If you want to restore your DB cluster using a DB cluster snapshot, modify the updated template with your DB cluster changes and add the <code>SnapshotIdentifier</code> property with the ID of the DB cluster snapshot that you want to use.<br />After you restore a DB cluster with a <code>SnapshotIdentifier</code> property, you must specify the same <code>SnapshotIdentifier</code> property for any future updates to the DB cluster. When you specify this property for an update, the DB cluster is not restored from the DB cluster snapshot again, and the data in the database is not changed. However, if you don't specify the <code>SnapshotIdentifier</code> property, an empty DB cluster is created, and the original DB cluster is deleted. If you specify a property that is different from the previous snapshot restore property, a new DB cluster is restored from the specified <code>SnapshotIdentifier</code> property, and the original DB cluster is deleted.<br />1. Update the stack.<br /><br />Currently, when you are updating the stack for an Aurora Serverless DB cluster, you can't include changes to any other properties when you specify one of the following properties: <code>PreferredBackupWindow</code>, <code>PreferredMaintenanceWindow</code>, and <code>Port</code>. This limitation doesn't apply to provisioned DB clusters.<br />For more information about updating other properties of this resource, see <code>ModifyDBCluster</code>. For more information about updating stacks, see &#91;CloudFormation Stacks Updates&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks.html).<br />*Deleting DB clusters* <br />The default <code>DeletionPolicy</code> for <code>AWS::RDS::DBCluster</code> resources is <code>Snapshot</code>. For more information about how AWS CloudFormation deletes resources, see &#91;DeletionPolicy Attribute&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html).</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rds.db_clusters_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="db_cluster_identifier" /></td><td><code>string</code></td><td>The DB cluster identifier. This parameter is stored as a lowercase string.<br />Constraints:<br />+ Must contain from 1 to 63 letters, numbers, or hyphens.<br />+ First character must be a letter.<br />+ Can't end with a hyphen or contain two consecutive hyphens.<br /><br />Example: <code>my-cluster1</code> <br />Valid for: Aurora DB clusters and Multi-AZ DB clusters</td></tr>
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
Lists all <code>db_clusters</code> in a region.
```sql
SELECT
region,
db_cluster_identifier
FROM aws.rds.db_clusters_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>db_clusters_list_only</code> resource, see <a href="/providers/aws/rds/db_clusters/#permissions"><code>db_clusters</code></a>

