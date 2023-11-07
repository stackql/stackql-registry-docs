---
title: db_cluster
hide_title: false
hide_table_of_contents: false
keywords:
  - db_cluster
  - docdb
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>db_cluster</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_cluster</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>db_cluster</td></tr>
<tr><td><b>Id</b></td><td><code>aws.docdb.db_cluster</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>StorageEncrypted</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>RestoreToTime</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>SnapshotIdentifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Port</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>DBClusterIdentifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>PreferredBackupWindow</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ClusterResourceId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Endpoint</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>VpcSecurityGroupIds</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>CopyTagsToSnapshot</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>RestoreType</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>EngineVersion</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>KmsKeyId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>AvailabilityZones</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>PreferredMaintenanceWindow</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>DBSubnetGroupName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>DeletionProtection</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>UseLatestRestorableTime</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>MasterUserPassword</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>SourceDBClusterIdentifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>MasterUsername</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ReadEndpoint</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>DBClusterParameterGroupName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>BackupRetentionPeriod</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>EnableCloudwatchLogsExports</code></td><td><code>array</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.docdb.db_cluster
WHERE region = 'us-east-1' AND data__Identifier = '&lt;Id&gt;'
</pre>
