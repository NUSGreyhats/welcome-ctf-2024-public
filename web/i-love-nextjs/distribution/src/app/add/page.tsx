'use client'

import { useFormStatus, useFormState } from 'react-dom'
import { addTagline } from '@/app/actions'

const initialState = {
  message: '',
}

export default function AddTagline() {
  const [state, formAction] = useFormState(addTagline, initialState)
  const { pending } = useFormStatus()

  return (
    <form action={formAction}>
      <label htmlFor="username">Username:</label>
      <br />
      <input type="text" id="username" name="username" required />
      <br />
      <br />
      <label htmlFor="Tagline">Tagline:</label>
      <br />
      <input type="text" id="tagline" name="tagline" required />
      <br />
      <button type="submit" aria-disabled={pending}>
        Add
      </button>
      <p aria-live="polite" role="status">
        {state.message}
      </p>
    </form>
  )
}
