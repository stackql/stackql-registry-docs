---
title: saas
hide_title: false
hide_table_of_contents: false
keywords:
  - saas
  - saas
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

Creates, updates, deletes, gets or lists a <code>saas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>saas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.saas.saas" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceId" /> | Deletes the specified SaaS. |

## `DELETE` example

Deletes the specified <code>saas</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.saas.saas
WHERE resourceId = '{{ resourceId }}';
```
