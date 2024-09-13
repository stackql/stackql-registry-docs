---
title: resourcefiles_environment_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - resourcefiles_environment_resources
  - apigee
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

Creates, updates, deletes, gets or lists a <code>resourcefiles_environment_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resourcefiles_environment_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.resourcefiles_environment_resources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="resourceFile" /> | `array` | List of resources files. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_environments_resourcefiles_list_environment_resources" /> | `SELECT` | <CopyableCode code="environmentsId, organizationsId, type" /> | Lists all resource files, optionally filtering by type. For more information about resource files, see [Resource files](https://cloud.google.com/apigee/docs/api-platform/develop/resource-files). |

## `SELECT` examples

Lists all resource files, optionally filtering by type. For more information about resource files, see [Resource files](https://cloud.google.com/apigee/docs/api-platform/develop/resource-files).

```sql
SELECT
resourceFile
FROM google.apigee.resourcefiles_environment_resources
WHERE environmentsId = '{{ environmentsId }}'
AND organizationsId = '{{ organizationsId }}'
AND type = '{{ type }}'; 
```
