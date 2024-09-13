---
title: clusters_master
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters_master
  - container
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

Creates, updates, deletes, gets or lists a <code>clusters_master</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters_master</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.container.clusters_master" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_clusters_update_master" /> | `UPDATE` | <CopyableCode code="clustersId, locationsId, projectsId" /> | Updates the master for a specific cluster. |

## `UPDATE` example

Updates a <code>clusters_master</code> resource.

```sql
/*+ update */
UPDATE google.container.clusters_master
SET 
projectId = '{{ projectId }}',
zone = '{{ zone }}',
clusterId = '{{ clusterId }}',
masterVersion = '{{ masterVersion }}',
name = '{{ name }}'
WHERE 
clustersId = '{{ clustersId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
