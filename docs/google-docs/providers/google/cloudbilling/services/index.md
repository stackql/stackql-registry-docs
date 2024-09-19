---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - cloudbilling
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

Creates, updates, deletes, gets or lists a <code>services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudbilling.services" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name for the service. Example: "services/6F81-5844-456A" |
| <CopyableCode code="businessEntityName" /> | `string` | The business under which the service is offered. Ex. "businessEntities/GCP", "businessEntities/Maps" |
| <CopyableCode code="displayName" /> | `string` | A human readable display name for this service. |
| <CopyableCode code="serviceId" /> | `string` | The identifier for the service. Example: "6F81-5844-456A" |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Lists all public cloud services. |

## `SELECT` examples

Lists all public cloud services.

```sql
SELECT
name,
businessEntityName,
displayName,
serviceId
FROM google.cloudbilling.services
;
```
