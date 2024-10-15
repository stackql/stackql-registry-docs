---
title: proxy_artifact_states
hide_title: false
hide_table_of_contents: false
keywords:
  - proxy_artifact_states
  - hybrid_network
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

Creates, updates, deletes, gets or lists a <code>proxy_artifact_states</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>proxy_artifact_states</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_network.proxy_artifact_states" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="artifactName, artifactStoreName, artifactVersionName, publisherName, resourceGroupName, subscriptionId" /> | Change artifact state defined in artifact store. |

## `UPDATE` example

Updates a <code>proxy_artifact_states</code> resource.

```sql
/*+ update */
UPDATE azure.hybrid_network.proxy_artifact_states
SET 
properties = '{{ properties }}'
WHERE 
artifactName = '{{ artifactName }}'
AND artifactStoreName = '{{ artifactStoreName }}'
AND artifactVersionName = '{{ artifactVersionName }}'
AND publisherName = '{{ publisherName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
