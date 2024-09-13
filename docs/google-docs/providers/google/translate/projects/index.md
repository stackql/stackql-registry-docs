
---
title: projects
hide_title: false
hide_table_of_contents: false
keywords:
  - projects
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

Creates, updates, deletes or gets an <code>project</code> resource or lists <code>projects</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>projects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.translate.projects" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_detect_language" /> | `EXEC` | <CopyableCode code="projectsId" /> | Detects the language of text within a request. |
| <CopyableCode code="projects_romanize_text" /> | `EXEC` | <CopyableCode code="projectsId" /> | Romanize input text written in non-Latin scripts to Latin text. |
| <CopyableCode code="projects_translate_text" /> | `EXEC` | <CopyableCode code="projectsId" /> | Translates input text and returns translated text. |
