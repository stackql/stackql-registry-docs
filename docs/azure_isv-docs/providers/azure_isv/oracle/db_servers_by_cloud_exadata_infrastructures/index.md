---
title: db_servers_by_cloud_exadata_infrastructures
hide_title: false
hide_table_of_contents: false
keywords:
  - db_servers_by_cloud_exadata_infrastructures
  - oracle
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

Creates, updates, deletes, gets or lists a <code>db_servers_by_cloud_exadata_infrastructures</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_servers_by_cloud_exadata_infrastructures</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.oracle.db_servers_by_cloud_exadata_infrastructures" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | DbServer resource properties |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="cloudexadatainfrastructurename, resourceGroupName, subscriptionId" /> | List DbServer resources by CloudExadataInfrastructure |

## `SELECT` examples

List DbServer resources by CloudExadataInfrastructure


```sql
SELECT
properties
FROM azure_isv.oracle.db_servers_by_cloud_exadata_infrastructures
WHERE cloudexadatainfrastructurename = '{{ cloudexadatainfrastructurename }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```