---
title: instances_parameters
hide_title: false
hide_table_of_contents: false
keywords:
  - instances_parameters
  - memcache
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

Creates, updates, deletes, gets or lists a <code>instances_parameters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instances_parameters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.memcache.instances_parameters" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="update_parameters" /> | `UPDATE` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Updates the defined Memcached parameters for an existing instance. This method only stages the parameters, it must be followed by `ApplyParameters` to apply the parameters to nodes of the Memcached instance. |

## `UPDATE` example

Updates a <code>instances_parameters</code> resource.

```sql
/*+ update */
UPDATE google.memcache.instances_parameters
SET 
updateMask = '{{ updateMask }}',
parameters = '{{ parameters }}'
WHERE 
instancesId = '{{ instancesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
