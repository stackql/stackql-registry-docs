---
title: repositories_history
hide_title: false
hide_table_of_contents: false
keywords:
  - repositories_history
  - dataform
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

Creates, updates, deletes, gets or lists a <code>repositories_history</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>repositories_history</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataform.repositories_history" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="commits" /> | `array` | A list of commit logs, ordered by 'git log' default order. |
| <CopyableCode code="nextPageToken" /> | `string` | A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="fetch_history" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, repositoriesId" /> | Fetches a Repository's history of commits. The Repository must not have a value for `git_remote_settings.url`. |

## `SELECT` examples

Fetches a Repository's history of commits. The Repository must not have a value for `git_remote_settings.url`.

```sql
SELECT
commits,
nextPageToken
FROM google.dataform.repositories_history
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND repositoriesId = '{{ repositoriesId }}';
```
