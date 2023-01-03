---
title: debugger_debuggees_breakpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - debugger_debuggees_breakpoints
  - clouddebugger
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
<tr><td><b>Name</b></td><td><code>debugger_debuggees_breakpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.clouddebugger.debugger_debuggees_breakpoints</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `breakpointId, debuggeeId` | Gets breakpoint information. |
| `list` | `SELECT` | `debuggeeId` | Lists all breakpoints for the debuggee. |
| `delete` | `DELETE` | `breakpointId, debuggeeId` | Deletes the breakpoint from the debuggee. |
| `set` | `EXEC` | `debuggeeId` | Sets the breakpoint to the debuggee. |
