---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - professional_services
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

Creates, updates, deletes, gets or lists a <code>operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.professional_services.operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | the operation name |
| <CopyableCode code="display" /> | `object` | ProfessionalService app operation display |
| <CopyableCode code="isDataAction" /> | `boolean` | whether the operation is a data action or not. |
| <CopyableCode code="origin" /> | `string` | the operation origin |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Gets all ProfessionalService app operations. |

## `SELECT` examples

Gets all ProfessionalService app operations.


```sql
SELECT
name,
display,
isDataAction,
origin
FROM azure_extras.professional_services.operations
;
```