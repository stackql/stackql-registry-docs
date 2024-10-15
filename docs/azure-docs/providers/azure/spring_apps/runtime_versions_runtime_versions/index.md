---
title: runtime_versions_runtime_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - runtime_versions_runtime_versions
  - spring_apps
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

Creates, updates, deletes, gets or lists a <code>runtime_versions_runtime_versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>runtime_versions_runtime_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.runtime_versions_runtime_versions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="platform" /> | `string` | The platform of this runtime version (possible values: "Java" or ".NET"). |
| <CopyableCode code="value" /> | `string` | The raw value which could be passed to deployment CRUD operations. |
| <CopyableCode code="version" /> | `string` | The detailed version (major.minor) of the platform. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Lists all of the available runtime versions supported by Microsoft.AppPlatform provider. |

## `SELECT` examples

Lists all of the available runtime versions supported by Microsoft.AppPlatform provider.


```sql
SELECT
platform,
value,
version
FROM azure.spring_apps.runtime_versions_runtime_versions
;
```