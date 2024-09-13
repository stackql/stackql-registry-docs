---
title: revisions_shared_flow_revision
hide_title: false
hide_table_of_contents: false
keywords:
  - revisions_shared_flow_revision
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

Creates, updates, deletes or gets an <code>revisions_shared_flow_revision</code> resource or lists <code>revisions_shared_flow_revision</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>revisions_shared_flow_revision</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.revisions_shared_flow_revision" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_sharedflows_revisions_update_shared_flow_revision" /> | `UPDATE` | <CopyableCode code="organizationsId, revisionsId, sharedflowsId" /> | Updates a shared flow revision. This operation is only allowed on revisions which have never been deployed. After deployment a revision becomes immutable, even if it becomes undeployed. The payload is a ZIP-formatted shared flow. Content type must be either multipart/form-data or application/octet-stream. |

## `UPDATE` example

Updates a revisions_shared_flow_revision only if the necessary resources are available.

```sql
UPDATE google.apigee.revisions_shared_flow_revision
SET 
contentType = '{{ contentType }}',
extensions = '{{ extensions }}',
data = '{{ data }}'
WHERE 
organizationsId = '{{ organizationsId }}'
AND revisionsId = '{{ revisionsId }}'
AND sharedflowsId = '{{ sharedflowsId }}';
```
