---
title: ado_oauth_info
hide_title: false
hide_table_of_contents: false
keywords:
  - ado_oauth_info
  - developer_hub
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

Creates, updates, deletes, gets or lists a <code>ado_oauth_info</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ado_oauth_info</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.developer_hub.ado_oauth_info" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="authURL" /> | `string` | URL used to authorize ADO app using Entra ID |
| <CopyableCode code="token" /> | `string` | OAuth token used to make calls to ADO APIs |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> |  |

## `SELECT` examples




```sql
SELECT
authURL,
token
FROM azure_extras.developer_hub.ado_oauth_info
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```