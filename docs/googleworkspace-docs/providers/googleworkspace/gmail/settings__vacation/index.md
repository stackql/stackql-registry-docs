---
title: settings__vacation
hide_title: false
hide_table_of_contents: false
keywords:
  - settings__vacation
  - gmail
  - googleworkspace    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleworkspace/stackql-googleworkspace-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>settings__vacation</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.gmail.settings__vacation</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `responseSubject` | `string` | Optional text to prepend to the subject line in vacation responses. In order to enable auto-replies, either the response subject or the response body must be nonempty. |
| `restrictToContacts` | `boolean` | Flag that determines whether responses are sent to recipients who are not in the user's list of contacts. |
| `restrictToDomain` | `boolean` | Flag that determines whether responses are sent to recipients who are outside of the user's domain. This feature is only available for G Suite users. |
| `startTime` | `string` | An optional start time for sending auto-replies (epoch ms). When this is specified, Gmail will automatically reply only to messages that it receives after the start time. If both `startTime` and `endTime` are specified, `startTime` must precede `endTime`. |
| `enableAutoReply` | `boolean` | Flag that controls whether Gmail automatically replies to messages. |
| `endTime` | `string` | An optional end time for sending auto-replies (epoch ms). When this is specified, Gmail will automatically reply only to messages that it receives before the end time. If both `startTime` and `endTime` are specified, `startTime` must precede `endTime`. |
| `responseBodyHtml` | `string` | Response body in HTML format. Gmail will sanitize the HTML before storing it. If both `response_body_plain_text` and `response_body_html` are specified, `response_body_html` will be used. |
| `responseBodyPlainText` | `string` | Response body in plain text format. If both `response_body_plain_text` and `response_body_html` are specified, `response_body_html` will be used. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `users_settings_getVacation` | `SELECT` | `userId` |
