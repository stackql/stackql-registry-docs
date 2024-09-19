---
title: entitlements
hide_title: false
hide_table_of_contents: false
keywords:
  - entitlements
  - oracledatabase
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

Creates, updates, deletes, gets or lists a <code>entitlements</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>entitlements</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.oracledatabase.entitlements" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. The name of the Entitlement resource with the format: projects/{project}/locations/{region}/entitlements/{entitlement} |
| <CopyableCode code="cloudAccountDetails" /> | `object` | Details of the OCI Cloud Account. |
| <CopyableCode code="entitlementId" /> | `string` | Output only. Google Cloud Marketplace order ID (aka entitlement ID) |
| <CopyableCode code="state" /> | `string` | Output only. Entitlement State. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists the entitlements in a given project. |

## `SELECT` examples

Lists the entitlements in a given project.

```sql
SELECT
name,
cloudAccountDetails,
entitlementId,
state
FROM google.oracledatabase.entitlements
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
