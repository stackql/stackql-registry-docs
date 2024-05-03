---
title: projects__analytics_details
hide_title: false
hide_table_of_contents: false
keywords:
  - projects__analytics_details
  - firebase
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
<tr><td><b>Name</b></td><td><code>projects__analytics_details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="firebase.firebase.projects__analytics_details" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="analyticsProperty" /> | `object` | Details of a Google Analytics property |
| <CopyableCode code="streamMappings" /> | `array` |  - For `AndroidApps` and `IosApps`: a map of `app` to `streamId` for each Firebase App in the specified `FirebaseProject`. Each `app` and `streamId` appears only once. - For `WebApps`: a map of `app` to `streamId` and `measurementId` for each `WebApp` in the specified `FirebaseProject`. Each `app`, `streamId`, and `measurementId` appears only once. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="projects_getAnalyticsDetails" /> | `SELECT` | <CopyableCode code="projectsId" /> |
