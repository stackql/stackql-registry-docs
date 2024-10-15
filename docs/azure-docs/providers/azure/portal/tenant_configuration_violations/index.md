---
title: tenant_configuration_violations
hide_title: false
hide_table_of_contents: false
keywords:
  - tenant_configuration_violations
  - portal
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

Creates, updates, deletes, gets or lists a <code>tenant_configuration_violations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tenant_configuration_violations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.portal.tenant_configuration_violations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Id of the item that violates tenant configuration. |
| <CopyableCode code="errorMessage" /> | `string` | Error message. |
| <CopyableCode code="userId" /> | `string` | Id of the user who owns violated item. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Gets list of items that violate tenant's configuration. |

## `SELECT` examples

Gets list of items that violate tenant's configuration.


```sql
SELECT
id,
errorMessage,
userId
FROM azure.portal.tenant_configuration_violations
;
```