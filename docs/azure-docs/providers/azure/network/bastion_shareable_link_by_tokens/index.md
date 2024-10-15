---
title: bastion_shareable_link_by_tokens
hide_title: false
hide_table_of_contents: false
keywords:
  - bastion_shareable_link_by_tokens
  - network
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

Creates, updates, deletes, gets or lists a <code>bastion_shareable_link_by_tokens</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bastion_shareable_link_by_tokens</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.bastion_shareable_link_by_tokens" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="bastionHostName, resourceGroupName, subscriptionId" /> | Deletes the Bastion Shareable Links for all the tokens specified in the request. |

## `DELETE` example

Deletes the specified <code>bastion_shareable_link_by_tokens</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.bastion_shareable_link_by_tokens
WHERE bastionHostName = '{{ bastionHostName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
