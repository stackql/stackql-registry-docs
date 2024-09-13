---
title: caches
hide_title: false
hide_table_of_contents: false
keywords:
  - caches
  - apigee
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

Creates, updates, deletes, gets or lists a <code>caches</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>caches</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.caches" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_environments_caches_delete" /> | `DELETE` | <CopyableCode code="cachesId, environmentsId, organizationsId" /> | Deletes a cache. |

## `DELETE` example

Deletes the specified <code>caches</code> resource.

```sql
/*+ delete */
DELETE FROM google.apigee.caches
WHERE cachesId = '{{ cachesId }}'
AND environmentsId = '{{ environmentsId }}'
AND organizationsId = '{{ organizationsId }}';
```
