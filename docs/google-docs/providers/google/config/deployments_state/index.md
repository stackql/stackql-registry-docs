---
title: deployments_state
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments_state
  - config
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

Creates, updates, deletes, gets or lists a <code>deployments_state</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployments_state</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.config.deployments_state" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="delete_state" /> | `DELETE` | <CopyableCode code="deploymentsId, locationsId, projectsId" /> | Deletes Terraform state file in a given deployment. |

## `DELETE` example

Deletes the specified <code>deployments_state</code> resource.

```sql
/*+ delete */
DELETE FROM google.config.deployments_state
WHERE deploymentsId = '{{ deploymentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
