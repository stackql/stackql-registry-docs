---
title: releases__executable
hide_title: false
hide_table_of_contents: false
keywords:
  - releases__executable
  - firebaserules
  - firebase    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/firebase/stackql-firebase-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>releases__executable</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="firebase.firebaserules.releases__executable" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="executable" /> | `string` | Executable view of the `Ruleset` referenced by the `Release`. |
| <CopyableCode code="executableVersion" /> | `string` | The Rules runtime version of the executable. |
| <CopyableCode code="language" /> | `string` | `Language` used to generate the executable bytes. |
| <CopyableCode code="rulesetName" /> | `string` | `Ruleset` name associated with the `Release` executable. |
| <CopyableCode code="syncTime" /> | `string` | Optional, indicates the freshness of the result. The response is guaranteed to be the latest within an interval up to the sync_time (inclusive). |
| <CopyableCode code="updateTime" /> | `string` | Timestamp for the most recent `Release.update_time`. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="projects_releases_getExecutable" /> | `SELECT` | <CopyableCode code="projectsId, releasesId" /> |
