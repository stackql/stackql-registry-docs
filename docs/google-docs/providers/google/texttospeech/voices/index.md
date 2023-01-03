---
title: voices
hide_title: false
hide_table_of_contents: false
keywords:
  - voices
  - texttospeech
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
<tr><td><b>Name</b></td><td><code>voices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.texttospeech.voices</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of this voice. Each distinct voice has a unique name. |
| `ssmlGender` | `string` | The gender of this voice. |
| `languageCodes` | `array` | The languages that this voice supports, expressed as [BCP-47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt) language tags (e.g. "en-US", "es-419", "cmn-tw"). |
| `naturalSampleRateHertz` | `integer` | The natural sample rate (in hertz) for this voice. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` |  |
