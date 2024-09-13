---
title: authorized_domains
hide_title: false
hide_table_of_contents: false
keywords:
  - authorized_domains
  - appengine
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

Creates, updates, deletes, gets or lists a <code>authorized_domains</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>authorized_domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.appengine.authorized_domains" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified domain name of the domain authorized for use. Example: example.com. |
| <CopyableCode code="name" /> | `string` | Full path to the AuthorizedDomain resource in the API. Example: apps/myapp/authorizedDomains/example.com.@OutputOnly |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="applicationsId, locationsId, projectsId" /> | Lists all domains the user is authorized to administer. |

## `SELECT` examples

Lists all domains the user is authorized to administer.

```sql
SELECT
id,
name
FROM google.appengine.authorized_domains
WHERE applicationsId = '{{ applicationsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```
