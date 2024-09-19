---
title: nodes_guest_attributes
hide_title: false
hide_table_of_contents: false
keywords:
  - nodes_guest_attributes
  - tpu
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

Creates, updates, deletes, gets or lists a <code>nodes_guest_attributes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>nodes_guest_attributes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.tpu.nodes_guest_attributes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="guestAttributes" /> | `array` | The guest attributes for the TPU workers. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_guest_attributes" /> | `SELECT` | <CopyableCode code="locationsId, nodesId, projectsId" /> | Retrieves the guest attributes for the node. |

## `SELECT` examples

Retrieves the guest attributes for the node.

```sql
SELECT
guestAttributes
FROM google.tpu.nodes_guest_attributes
WHERE locationsId = '{{ locationsId }}'
AND nodesId = '{{ nodesId }}'
AND projectsId = '{{ projectsId }}';
```
