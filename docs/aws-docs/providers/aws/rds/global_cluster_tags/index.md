---
title: global_cluster_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - global_cluster_tags
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

Expands all tag keys and values for <code>global_clusters</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>global_cluster_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::RDS::GlobalCluster</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rds.global_cluster_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="engine" /></td><td><code>string</code></td><td>The name of the database engine to be used for this DB cluster. Valid Values: aurora (for MySQL 5.6-compatible Aurora), aurora-mysql (for MySQL 5.7-compatible Aurora).<br />If you specify the SourceDBClusterIdentifier property, don't specify this property. The value is inherited from the cluster.</td></tr>
<tr><td><CopyableCode code="engine_lifecycle_support" /></td><td><code>string</code></td><td>The life cycle type of the global cluster. You can use this setting to enroll your global cluster into Amazon RDS Extended Support.</td></tr>
<tr><td><CopyableCode code="engine_version" /></td><td><code>string</code></td><td>The version number of the database engine to use. If you specify the SourceDBClusterIdentifier property, don't specify this property. The value is inherited from the cluster.</td></tr>
<tr><td><CopyableCode code="deletion_protection" /></td><td><code>boolean</code></td><td>The deletion protection setting for the new global database. The global database can't be deleted when deletion protection is enabled.</td></tr>
<tr><td><CopyableCode code="global_cluster_identifier" /></td><td><code>string</code></td><td>The cluster identifier of the new global database cluster. This parameter is stored as a lowercase string.</td></tr>
<tr><td><CopyableCode code="source_db_cluster_identifier" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) to use as the primary cluster of the global database. This parameter is optional. This parameter is stored as a lowercase string.</td></tr>
<tr><td><CopyableCode code="storage_encrypted" /></td><td><code>boolean</code></td><td>The storage encryption setting for the new global database cluster.<br />If you specify the SourceDBClusterIdentifier property, don't specify this property. The value is inherited from the cluster.</td></tr>
<tr><td><CopyableCode code="global_endpoint" /></td><td><code>object</code></td><td></td></tr>
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
Expands tags for all <code>global_clusters</code> in a region.
```sql
SELECT
region,
engine,
engine_lifecycle_support,
engine_version,
deletion_protection,
global_cluster_identifier,
source_db_cluster_identifier,
storage_encrypted,
global_endpoint,
tag_key,
tag_value
FROM aws.rds.global_cluster_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>global_cluster_tags</code> resource, see <a href="/providers/aws/rds/global_clusters/#permissions"><code>global_clusters</code></a>

