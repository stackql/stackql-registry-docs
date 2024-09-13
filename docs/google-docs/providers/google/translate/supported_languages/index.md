---
title: supported_languages
hide_title: false
hide_table_of_contents: false
keywords:
  - supported_languages
  - translate
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

Creates, updates, deletes or gets an <code>supported_language</code> resource or lists <code>supported_languages</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>supported_languages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.translate.supported_languages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="languages" /> | `array` | A list of supported language responses. This list contains an entry for each language the Translation API supports. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_get_supported_languages" /> | `SELECT` | <CopyableCode code="projectsId" /> | Returns a list of supported languages for translation. |
| <CopyableCode code="projects_locations_get_supported_languages" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Returns a list of supported languages for translation. |

## `SELECT` examples

Returns a list of supported languages for translation.

```sql
SELECT
languages
FROM google.translate.supported_languages
WHERE projectsId = '{{ projectsId }}'; 
```
