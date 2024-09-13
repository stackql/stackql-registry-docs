---
title: locations
hide_title: false
hide_table_of_contents: false
keywords:
  - locations
  - contactcenteraiplatform
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

Creates, updates, deletes, gets or lists a <code>locations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>locations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.contactcenteraiplatform.locations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="contactCenterCountLimit" /> | `integer` | Deprecated: Use the Quota fields instead. Reflects the count limit of contact centers on a billing account. |
| <CopyableCode code="contactCenterCountSum" /> | `integer` | Deprecated: Use the Quota fields instead. Reflects the count sum of contact centers on a billing account. |
| <CopyableCode code="quotas" /> | `array` | Quota details per contact center instance type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Gets information about a location. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists information about the supported locations for this service. |
| <CopyableCode code="query_contact_center_quota" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Queries the contact center quota, an aggregation over all the projects, that belongs to the billing account, which the input project belongs to. |

## `SELECT` examples

Lists information about the supported locations for this service.

```sql
SELECT
contactCenterCountLimit,
contactCenterCountSum,
quotas
FROM google.contactcenteraiplatform.locations
WHERE projectsId = '{{ projectsId }}'; 
```
