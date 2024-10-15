---
title: organization_schema_registry_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - organization_schema_registry_clusters
  - confluent
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

Creates, updates, deletes, gets or lists a <code>organization_schema_registry_clusters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>organization_schema_registry_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.confluent.organization_schema_registry_clusters" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Id of the cluster |
| <CopyableCode code="kind" /> | `string` | Kind of the cluster |
| <CopyableCode code="properties" /> | `object` | Schema Registry Cluster Properties |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="environmentId, organizationName, resourceGroupName, subscriptionId" /> |  |

## `SELECT` examples




```sql
SELECT
id,
kind,
properties
FROM azure_isv.confluent.organization_schema_registry_clusters
WHERE environmentId = '{{ environmentId }}'
AND organizationName = '{{ organizationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```