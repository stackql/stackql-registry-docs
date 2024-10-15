---
title: import_sites_controller_imported_machines
hide_title: false
hide_table_of_contents: false
keywords:
  - import_sites_controller_imported_machines
  - migrate
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

Creates, updates, deletes, gets or lists a <code>import_sites_controller_imported_machines</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>import_sites_controller_imported_machines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate.import_sites_controller_imported_machines" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | Deletes the imported machines for site. |

## `DELETE` example

Deletes the specified <code>import_sites_controller_imported_machines</code> resource.

```sql
/*+ delete */
DELETE FROM azure.migrate.import_sites_controller_imported_machines
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
