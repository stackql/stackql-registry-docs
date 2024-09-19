---
title: discovered_services
hide_title: false
hide_table_of_contents: false
keywords:
  - discovered_services
  - apphub
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

Creates, updates, deletes, gets or lists a <code>discovered_services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>discovered_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apphub.discovered_services" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. The resource name of the discovered service. Format: "projects/{host-project-id}/locations/{location}/discoveredServices/{uuid}"" |
| <CopyableCode code="serviceProperties" /> | `object` | Properties of an underlying cloud resource that can comprise a Service. |
| <CopyableCode code="serviceReference" /> | `object` | Reference to an underlying networking resource that can comprise a Service. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="discoveredServicesId, locationsId, projectsId" /> | Gets a Discovered Service in a host project and location. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists Discovered Services that can be added to an Application in a host project and location. |
| <CopyableCode code="lookup" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists a Discovered Service in a host project and location, with a given resource URI. |

## `SELECT` examples

Lists Discovered Services that can be added to an Application in a host project and location.

```sql
SELECT
name,
serviceProperties,
serviceReference
FROM google.apphub.discovered_services
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
