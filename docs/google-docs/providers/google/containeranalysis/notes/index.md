---
title: notes
hide_title: false
hide_table_of_contents: false
keywords:
  - notes
  - containeranalysis
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>notes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.containeranalysis.notes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The name of the note in the form of `projects/[PROVIDER_ID]/notes/[NOTE_ID]`. |
| `longDescription` | `string` | A detailed description of this note. |
| `package` | `object` | PackageNote represents a particular package version. |
| `shortDescription` | `string` | A one sentence description of this note. |
| `compliance` | `object` |  |
| `relatedNoteNames` | `array` | Other notes related to this note. |
| `createTime` | `string` | Output only. The time this note was created. This field can be used as a filter in list requests. |
| `vulnerability` | `object` | A security vulnerability that can be found in resources. |
| `build` | `object` | Note holding the version of the provider's builder and the signature of the provenance message in the build details occurrence. |
| `relatedUrl` | `array` | URLs associated with this note. |
| `upgrade` | `object` | An Upgrade Note represents a potential upgrade of a package to a given version. For each package version combination (i.e. bash 4.0, bash 4.1, bash 4.1.2), there will be an Upgrade Note. For Windows, windows_update field represents the information related to the update. |
| `deployment` | `object` | An artifact that can be deployed in some runtime. |
| `dsseAttestation` | `object` |  |
| `image` | `object` | Basis describes the base image portion (Note) of the DockerImage relationship. Linked occurrences are derived from this or an equivalent image via: FROM Or an equivalent reference, e.g., a tag of the resource_url. |
| `updateTime` | `string` | Output only. The time this note was last updated. This field can be used as a filter in list requests. |
| `kind` | `string` | Output only. The type of analysis. This field can be used as a filter in list requests. |
| `expirationTime` | `string` | Time of expiration for this note. Empty if note does not expire. |
| `discovery` | `object` | A note that indicates a type of analysis a provider would perform. This note exists in a provider's project. A `Discovery` occurrence is created in a consumer's project at the start of analysis. |
| `attestation` | `object` | Note kind that represents a logical attestation "role" or "authority". For example, an organization might have one `Authority` for "QA" and one for "build". This note is intended to act strictly as a grouping mechanism for the attached occurrences (Attestations). This grouping mechanism also provides a security boundary, since IAM ACLs gate the ability for a principle to attach an occurrence to a given note. It also provides a single point of lookup to find all attached attestation occurrences, even if they don't all live in the same project. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_notes_get` | `SELECT` | `notesId, projectsId` | Gets the specified note. |
| `projects_notes_list` | `SELECT` | `projectsId` | Lists notes for the specified project. |
| `projects_notes_create` | `INSERT` | `projectsId` | Creates a new note. |
| `projects_notes_delete` | `DELETE` | `notesId, projectsId` | Deletes the specified note. |
| `projects_notes_patch` | `EXEC` | `notesId, projectsId` | Updates the specified note. |
