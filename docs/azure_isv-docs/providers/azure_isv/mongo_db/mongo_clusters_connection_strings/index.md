---
title: mongo_clusters_connection_strings
hide_title: false
hide_table_of_contents: false
keywords:
  - mongo_clusters_connection_strings
  - mongo_db
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>mongo_clusters_connection_strings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>mongo_clusters_connection_strings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.mongo_db.mongo_clusters_connection_strings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="connectionStrings" /> | `array` | An array that contains the connection strings for a mongo cluster. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="mongoClusterName, resourceGroupName, subscriptionId" /> | List mongo cluster connection strings. This includes the default connection string using SCRAM-SHA-256, as well as other connection strings supported by the cluster. |

## `SELECT` examples

List mongo cluster connection strings. This includes the default connection string using SCRAM-SHA-256, as well as other connection strings supported by the cluster.


```sql
SELECT
connectionStrings
FROM azure_isv.mongo_db.mongo_clusters_connection_strings
WHERE mongoClusterName = '{{ mongoClusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```